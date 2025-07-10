import React, { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Shield, Upload, FileText, Settings, BarChart3, Download, AlertTriangle, CheckCircle, XCircle } from 'lucide-react'
import FileUpload from './components/FileUpload'
import ScanResults from './components/ScanResults'
import Dashboard from './components/Dashboard'
import Navbar from './components/Navbar'

function App() {
  const [scans, setScans] = useState([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    fetchScans()
  }, [])

  const fetchScans = async () => {
    try {
      const response = await fetch('/api/scans')
      const data = await response.json()
      setScans(data.scans || [])
    } catch (error) {
      console.error('Error fetching scans:', error)
    }
  }

  const handleScanComplete = () => {
    fetchScans() // Refresh the scans list
  }

  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        
        <div className="container mx-auto px-4 py-8">
          <Routes>
            <Route 
              path="/" 
              element={
                <Dashboard 
                  scans={scans}
                />
              } 
            />
            <Route 
              path="/upload" 
              element={
                <FileUpload 
                  onScanComplete={handleScanComplete}
                  loading={loading}
                  setLoading={setLoading}
                />
              } 
            />
            <Route 
              path="/scan/:scanId" 
              element={
                <ScanResults />
              } 
            />
          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App
