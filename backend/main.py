from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import xml.etree.ElementTree as ET
import openai
import os
import json
import asyncio
from datetime import datetime
from typing import List, Dict, Any
import requests
from pydantic import BaseModel
import uuid

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Vulnerability Patch Management LLM", version="1.0.0")

# CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Data models
class ServiceInfo(BaseModel):
    ip: str
    port: str
    service: str
    version: str
    recommendation: str = ""
    severity: str = "Unknown"
    cve_info: List[str] = []

class ScanResult(BaseModel):
    scan_id: str
    timestamp: str
    services: List[ServiceInfo]
    summary: Dict[str, Any]

# In-memory storage for demo (use database in production)
scan_results = {}

def parse_nmap_xml(xml_content: str) -> List[Dict[str, str]]:
    """Parse Nmap XML and extract service information"""
    try:
        root = ET.fromstring(xml_content)
        results = []
        
        for host in root.findall("host"):
            # Get IP address
            address_elem = host.find("address")
            if address_elem is None:
                continue
            ip = address_elem.attrib.get("addr", "Unknown")
            
            # Get ports and services
            for port in host.findall(".//port"):
                port_num = port.attrib.get("portid", "")
                state = port.find("state")
                if state is None or state.attrib.get("state") != "open":
                    continue
                    
                service_elem = port.find("service")
                if service_elem is not None:
                    service_name = service_elem.attrib.get("name", "")
                    version = service_elem.attrib.get("version", "")
                    product = service_elem.attrib.get("product", "")
                    
                    if service_name:  # Only include if service is detected
                        results.append({
                            "ip": ip,
                            "port": port_num,
                            "service": service_name,
                            "version": version,
                            "product": product
                        })
        
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse XML: {str(e)}")

async def get_cve_info(service: str, version: str) -> List[str]:
    """Get CVE information from NVD API"""
    try:
        # Search for CVEs related to the service and version
        query = f"{service} {version}"
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0"
        params = {
            "keywordSearch": query,
            "resultsPerPage": 5
        }
        
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            cves = []
            for vuln in data.get("vulnerabilities", []):
                cve_id = vuln.get("cve", {}).get("id", "")
                description = vuln.get("cve", {}).get("descriptions", [{}])[0].get("value", "")
                cves.append(f"{cve_id}: {description[:100]}...")
            return cves
    except:
        pass
    return []

def determine_severity(service: str, version: str, cve_count: int) -> str:
    """Determine severity based on service, version, and CVE count"""
    high_risk_services = ["ssh", "telnet", "ftp", "smtp", "pop3", "imap"]
    medium_risk_services = ["http", "https", "dns", "ntp"]
    
    if service.lower() in high_risk_services:
        return "High"
    elif service.lower() in medium_risk_services:
        return "Medium"
    elif cve_count > 0:
        return "Medium"
    else:
        return "Low"

async def get_llm_recommendation(service: str, version: str, cve_info: List[str]) -> str:
    """Get patch recommendations from LLM"""
    if not openai.api_key:
        return "OpenAI API key not configured. Please set OPENAI_API_KEY environment variable."
    
    try:
        cve_text = "\n".join(cve_info) if cve_info else "No known CVEs found"
        
        prompt = f"""
You are a cybersecurity expert. Analyze the following service and provide detailed patch recommendations:

Service: {service}
Version: {version}
Known CVEs: {cve_text}

Please provide:
1. Security assessment
2. Specific patch/upgrade steps
3. Alternative security measures
4. Risk level explanation

Format your response in a clear, actionable manner.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cybersecurity expert specializing in vulnerability assessment and patch management."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.3
        )
        
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error getting LLM recommendation: {str(e)}"

async def generate_patch_script(service: str, version: str) -> str:
    """Generate automated patch script using LLM"""
    if not openai.api_key:
        return "# OpenAI API key not configured"
    
    try:
        prompt = f"""
Generate a Linux shell script to patch/upgrade {service} version {version}.
The script should:
1. Check current version
2. Backup current configuration
3. Update/upgrade the service
4. Verify the update
5. Include error handling

Provide only the shell script code, no explanations.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a DevOps expert. Generate only shell script code."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.2
        )
        
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"# Error generating script: {str(e)}"

@app.post("/api/parse-scan")
async def parse_scan(file: UploadFile = File(...)):
    """Parse Nmap XML file and generate vulnerability report"""
    if not file.filename.endswith('.xml'):
        raise HTTPException(status_code=400, detail="File must be an XML file")
    
    try:
        xml_content = await file.read()
        xml_text = xml_content.decode('utf-8')
        
        # Parse XML
        services_data = parse_nmap_xml(xml_text)
        
        # Generate scan ID
        scan_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        # Process each service
        processed_services = []
        for service_data in services_data:
            # Get CVE information
            cve_info = await get_cve_info(service_data["service"], service_data["version"])
            
            # Get LLM recommendation
            recommendation = await get_llm_recommendation(
                service_data["service"], 
                service_data["version"], 
                cve_info
            )
            
            # Determine severity
            severity = determine_severity(
                service_data["service"], 
                service_data["version"], 
                len(cve_info)
            )
            
            # Create service info
            service_info = ServiceInfo(
                ip=service_data["ip"],
                port=service_data["port"],
                service=service_data["service"],
                version=service_data["version"],
                recommendation=recommendation,
                severity=severity,
                cve_info=cve_info
            )
            processed_services.append(service_info)
        
        # Generate summary
        severity_counts = {}
        for service in processed_services:
            severity_counts[service.severity] = severity_counts.get(service.severity, 0) + 1
        
        summary = {
            "total_services": len(processed_services),
            "severity_breakdown": severity_counts,
            "high_risk_count": severity_counts.get("High", 0),
            "medium_risk_count": severity_counts.get("Medium", 0),
            "low_risk_count": severity_counts.get("Low", 0)
        }
        
        # Store results
        scan_results[scan_id] = ScanResult(
            scan_id=scan_id,
            timestamp=timestamp,
            services=processed_services,
            summary=summary
        )
        
        return {
            "status": "success",
            "scan_id": scan_id,
            "timestamp": timestamp,
            "services": [service.dict() for service in processed_services],
            "summary": summary
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.get("/api/scan/{scan_id}")
async def get_scan_result(scan_id: str):
    """Get scan results by ID"""
    if scan_id not in scan_results:
        raise HTTPException(status_code=404, detail="Scan not found")
    
    return scan_results[scan_id]

@app.post("/api/generate-script/{scan_id}")
async def generate_script(scan_id: str, service_index: int):
    """Generate patch script for specific service"""
    if scan_id not in scan_results:
        raise HTTPException(status_code=404, detail="Scan not found")
    
    scan = scan_results[scan_id]
    if service_index >= len(scan.services):
        raise HTTPException(status_code=400, detail="Invalid service index")
    
    service = scan.services[service_index]
    script = await generate_patch_script(service.service, service.version)
    
    return {
        "service": service.service,
        "version": service.version,
        "script": script
    }

@app.get("/api/scans")
async def list_scans():
    """List all scan results"""
    return {
        "scans": [
            {
                "scan_id": scan_id,
                "timestamp": scan.timestamp,
                "summary": scan.summary
            }
            for scan_id, scan in scan_results.items()
        ]
    }

@app.delete("/api/scan/{scan_id}")
async def delete_scan(scan_id: str):
    """Delete scan result"""
    if scan_id not in scan_results:
        raise HTTPException(status_code=404, detail="Scan not found")
    
    del scan_results[scan_id]
    return {"status": "deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
