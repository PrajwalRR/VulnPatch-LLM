# 🔒 VulnPatch-LLM: AI-Powered Vulnerability Management Platform

A comprehensive vulnerability patch management platform that uses AI/LLM to analyze Nmap scan results and provide automated vulnerability assessment, patch recommendations, and interactive security guidance.

## 🚀 Features

### 🔐 Authentication & User Management
- **JWT-based Authentication**: Secure login/signup system
- **User-specific Data**: Each user has isolated scan data
- **Protected Routes**: Secure access to all features
- **Session Management**: Automatic token handling

### 📊 Advanced Analytics Dashboard
- **Real-time Statistics**: Total scans, services, and risk breakdown
- **Interactive Charts**: Timeline analysis and service distribution
- **Risk Analytics**: High, medium, and low risk service tracking
- **Top Services Analysis**: Most common vulnerable services

### 🤖 AI-Powered Chatbot
- **Interactive Conversations**: Chat with AI about vulnerabilities
- **Context-Aware Responses**: AI understands your scan data
- **Security Guidance**: Get expert advice on specific services
- **Real-time Assistance**: Instant answers to security questions

### 📄 Professional PDF Reports
- **Comprehensive Reports**: Detailed vulnerability analysis
- **Professional Formatting**: Clean, readable PDF exports
- **Service Details**: Complete vulnerability information
- **Recommendations**: AI-generated patch suggestions

### 🔧 Core Features
- **XML Parser**: Parse Nmap XML scan files
- **CVE Lookup**: Real-time CVE information from NVD API
- **LLM Analysis**: Groq Llama-3 powered vulnerability assessment
- **Automated Scripts**: Generate patch scripts for services
- **Modern UI**: Beautiful React frontend with Tailwind CSS
- **Real-time Processing**: Fast API backend with async processing
- **Severity Assessment**: Automatic risk level classification

## 📁 Project Structure

```
VulnPatch-LLM/
├── backend/
│   ├── main.py              # FastAPI backend server
│   ├── requirements.txt      # Python dependencies
│   └── README.md           # Backend setup instructions
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   │   ├── Dashboard.jsx      # Analytics dashboard
│   │   │   ├── FileUpload.jsx     # File upload component
│   │   │   ├── Navbar.jsx         # Navigation bar
│   │   │   ├── ScanResults.jsx    # Scan results display
│   │   │   └── Chatbot.jsx        # AI chatbot component
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
   GROQ_API_KEY=your_groq_api_key_here
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

### 1. **User Registration & Login**
- Create an account with username, email, and password
- Login to access all features
- All data is user-specific and secure

### 2. **Upload & Analyze Scans**
- Upload Nmap XML files through the drag & drop interface
- System automatically analyzes vulnerabilities using AI
- View detailed results with severity levels and recommendations

### 3. **Dashboard Analytics**
- View comprehensive statistics and charts
- Track scan history and risk trends
- Analyze top vulnerable services

### 4. **AI Chatbot Interaction**
- Chat with AI about your vulnerabilities
- Get context-aware security advice
- Ask specific questions about services and patches

### 5. **Generate & Export Reports**
- Generate automated patch scripts for services
- Export comprehensive PDF reports
- Download detailed vulnerability analysis

## 🔧 API Endpoints

### Authentication
- `POST /api/register` - User registration
- `POST /api/login` - User login
- `GET /api/me` - Get current user info

### Scan Management
- `POST /api/parse-scan` - Upload and parse Nmap XML
- `GET /api/scan/{scan_id}` - Get scan results
- `GET /api/scans` - List all user scans
- `DELETE /api/scan/{scan_id}` - Delete scan

### Scripts & Reports
- `POST /api/generate-script/{scan_id}` - Generate patch script

### Analytics
- `GET /api/stats/summary` - Get user statistics
- `GET /api/stats/timeline` - Get timeline data
- `GET /api/stats/top-services` - Get top services

### AI Chat
- `POST /api/chat` - Chat with AI about vulnerabilities

## 🎨 UI Features

### **Modern Dashboard**
- Real-time statistics and charts
- Interactive data visualization
- Risk breakdown analysis
- Timeline tracking

### **Secure Authentication**
- Clean login/signup forms
- JWT token management
- Protected route handling
- User session management

### **File Upload Interface**
- Drag & drop XML file upload
- Progress indicators
- File validation
- Error handling

### **Results Display**
- Detailed vulnerability analysis
- Service-specific information
- CVE data integration
- Severity classification

### **AI Chatbot**
- Interactive chat interface
- Context-aware responses
- Real-time AI assistance
- Security expert guidance

### **PDF Export**
- Professional report formatting
- Comprehensive vulnerability details
- Clean, readable layout
- Complete service information

## 🧪 Testing

Use the provided sample Nmap XML file:
```bash
# Test with the sample file (requires authentication)
curl -X POST -F "file=@examples/sample_nmap.xml" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  http://localhost:8000/api/parse-scan
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

- **JWT Authentication**: Secure token-based authentication
- **User Isolation**: Each user's data is completely isolated
- **CORS Configuration**: Secure frontend-backend communication
- **Input Validation**: Comprehensive validation for all inputs
- **Error Handling**: Secure error responses
- **Environment Variables**: Secure API key management

## 📊 Sample Output

The system provides:
- **User Management**: Secure authentication and user-specific data
- **Service Analysis**: IP, port, service name, version
- **CVE Information**: Known vulnerabilities from NVD database
- **AI Recommendations**: Detailed patch instructions from Groq Llama-3
- **Severity Levels**: High, Medium, Low risk classification
- **Automated Scripts**: Ready-to-use patch scripts
- **Analytics**: Comprehensive statistics and trends
- **Interactive Chat**: AI-powered security guidance
- **PDF Reports**: Professional vulnerability reports

## 🎯 Hackathon Deliverables ✅

- ✅ **User Authentication**: JWT-based login/signup system
- ✅ **Upload Nmap XML File**: Secure file upload with validation
- ✅ **Parse Services**: Comprehensive XML parsing
- ✅ **LLM Patch Suggestions**: AI-powered recommendations
- ✅ **Risk Report**: Detailed vulnerability analysis
- ✅ **Frontend UI**: Modern, responsive interface
- ✅ **Export Report**: Professional PDF exports
- ✅ **Patch Script Generator**: Automated script generation
- ✅ **Modern UI/UX**: Beautiful, intuitive design
- ✅ **Analytics Dashboard**: Comprehensive statistics and charts
- ✅ **AI Chatbot**: Interactive security assistance
- ✅ **User Management**: Secure, isolated user data

## 🛠️ Technologies Used

**Backend:**
- FastAPI (Python)
- Groq Llama-3 API
- NVD CVE API
- JWT Authentication
- XML parsing
- Pydantic models

**Frontend:**
- React 18
- Vite
- Tailwind CSS
- React Router
- Lucide React Icons
- React Dropzone
- React Markdown
- Syntax Highlighter
- Recharts (Analytics)
- jsPDF (PDF Export)
- jsPDF-AutoTable

**Authentication:**
- JWT tokens
- bcrypt password hashing
- OAuth2 password bearer

## 📝 License

This project is created for hackathon purposes.

---

**Ready to secure your infrastructure with AI-powered vulnerability management! 🚀**

*Built with ❤️ for the hackathon - A comprehensive solution for modern cybersecurity challenges.* 
