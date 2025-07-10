# Vulnerability Patch Management LLM - Backend

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
Create a `.env` file in the backend directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

3. Run the server:
```bash
python main.py
```

The server will start on `http://localhost:8000`

## API Endpoints

- `POST /api/parse-scan` - Upload and parse Nmap XML file
- `GET /api/scan/{scan_id}` - Get scan results by ID
- `POST /api/generate-script/{scan_id}` - Generate patch script for service
- `GET /api/scans` - List all scans
- `DELETE /api/scan/{scan_id}` - Delete scan result

## Features

- Parse Nmap XML files
- CVE lookup via NVD API
- LLM-powered vulnerability analysis
- Automated patch script generation
- Severity assessment
- Real-time recommendations 