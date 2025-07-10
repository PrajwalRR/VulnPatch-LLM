# 🔒 Vulnerability Patch Management using LLM

A comprehensive hackathon project that uses AI/LLM to analyze Nmap scan results and provide automated vulnerability assessment and patch recommendations.

## 🚀 Features

- **XML Parser**: Parse Nmap XML scan files
- **CVE Lookup**: Real-time CVE information from NVD API
- **LLM Analysis**: GPT-4 powered vulnerability assessment
- **Automated Scripts**: Generate patch scripts for services
- **Modern UI**: Beautiful React frontend with Tailwind CSS
- **Real-time Processing**: Fast API backend with async processing
- **Export Reports**: Download detailed vulnerability reports
- **Severity Assessment**: Automatic risk level classification

## 📁 Project Structure

```
Societe_Generale/
├── backend/
│   ├── main.py              # FastAPI backend server
│   ├── requirements.txt      # Python dependencies
│   └── README.md           # Backend setup instructions
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.jsx         # Main app component
│   │   └── index.css       # Tailwind styles
│   ├── package.json        # Node.js dependencies
│   ├── vite.config.js      # Vite configuration
│   └── tailwind.config.js  # Tailwind configuration
├── examples/
│   └── sample_nmap.xml     # Sample Nmap XML for testing
└── README.md              # This file
```

## 🛠️ Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the backend directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the backend server:**
   ```bash
   python main.py
   ```
   The server will start on `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```
   The frontend will start on `http://localhost:3000`

## 🎯 How to Use

1. **Upload Scan**: Go to the upload page and drag & drop your Nmap XML file
2. **AI Analysis**: The system will automatically analyze vulnerabilities using LLM
3. **View Results**: See detailed vulnerability assessment with severity levels
4. **Generate Scripts**: Get automated patch scripts for each service
5. **Export Reports**: Download comprehensive vulnerability reports

## 🔧 API Endpoints

- `POST /api/parse-scan` - Upload and parse Nmap XML
- `GET /api/scan/{scan_id}` - Get scan results
- `POST /api/generate-script/{scan_id}` - Generate patch script
- `GET /api/scans` - List all scans
- `DELETE /api/scan/{scan_id}` - Delete scan

## 🎨 UI Features

- **Dashboard**: Overview of all scans with statistics
- **File Upload**: Drag & drop interface for XML files
- **Results View**: Detailed vulnerability analysis
- **Script Generation**: Automated patch scripts with syntax highlighting
- **Export Functionality**: Download reports in Markdown format

## 🧪 Testing

Use the provided sample Nmap XML file:
```bash
# Test with the sample file
curl -X POST -F "file=@examples/sample_nmap.xml" http://localhost:8000/api/parse-scan
```

## 🚀 Deployment

### Backend (Production)
```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend (Production)
```bash
# Build for production
npm run build

# Serve static files
npm install -g serve
serve -s dist -l 3000
```

## 🔐 Security Features

- CORS enabled for frontend-backend communication
- Input validation for XML files
- Error handling for API calls
- Secure environment variable management

## 📊 Sample Output

The system provides:
- **Service Analysis**: IP, port, service name, version
- **CVE Information**: Known vulnerabilities from NVD database
- **LLM Recommendations**: Detailed patch instructions
- **Severity Levels**: High, Medium, Low risk classification
- **Automated Scripts**: Ready-to-use patch scripts

## 🎯 Hackathon Deliverables ✅

- ✅ Upload Nmap XML File
- ✅ Parse Services
- ✅ LLM Patch Suggestions
- ✅ Risk Report
- ✅ Frontend UI
- ✅ Export Report
- ✅ Patch Script Generator
- ✅ Modern UI/UX

## 🛠️ Technologies Used

**Backend:**
- FastAPI (Python)
- OpenAI GPT-4 API
- NVD CVE API
- XML parsing

**Frontend:**
- React 18
- Vite
- Tailwind CSS
- React Router
- Lucide React Icons
- React Dropzone
- React Markdown
- Syntax Highlighter

## 📝 License

This project is created for hackathon purposes.

---

**Ready to secure your infrastructure with AI-powered vulnerability management! 🚀** 