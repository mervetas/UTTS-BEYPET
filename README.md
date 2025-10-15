# UTTS Beypet - Fullstack Project

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.2.2-green)
![React](https://img.shields.io/badge/React-18.0+-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange)

A secure full-stack web application developed for Beypet, enabling technicians to access their vehicle assembly data through UTTS Portal integration.

## ✨ Core Features

### 🔐 Authentication & Security
- **Role-Based Technician Login** - Secure authentication system
- **Password Hashing with Bcrypt** - Encrypted credential storage
- **Session Management** - Secure user sessions
- **CORS Protection** - Cross-origin request security

### 📊 Data Management
- **Technician-Specific Data Access** - Users see only their assigned records
- **UTTS API Integration** - Real-time data synchronization
- **Vehicle Assembly Tracking** - Monitor assembly progress
- **MySQL Database** - Reliable data storage

### 🎨 User Experience
- **Responsive React Frontend** - Mobile-friendly interface
- **Dynamic Data Tables** - Search and filter capabilities
- **Real-time Data Updates** - Live data synchronization
- **Intuitive Dashboard** - Clean technician interface

### ⚙️ Admin Features
- **User Management** - Technician account control
- **Data Synchronization** - UTTS API integration management
- **Access Control** - Role-based permissions
- **System Monitoring** - Application health checks

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- MySQL Server

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/mervetas/UTTS-BEYPET.git
cd UTTS-BEYPET
```
2. **Backend Setup:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```
3. **Configure Environment:**
```bash
# Create .env file in backend directory with:
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=beypet_db
SECRET_KEY=your_secret_key
UTTS_API_URL=your_utts_api_url
UTTS_API_KEY=your_utts_api_key
```
4. **Frontend Setup:**
```bash
cd frontend
npm install
```
5. **Run Development Servers:**
```bash
# Backend (Terminal 1)
cd backend
venv\Scripts\activate
python app.py

# Frontend (Terminal 2)
cd frontend
npm start
```
6. **Access the Application:**
Frontend: http://localhost:3000

Backend API: http://localhost:5000

### 📁 Project Structure
```text
UTTS-BEYPET/
├── backend/                                # Flask Backend API
│ ├── controllers/                          # API route handlers
│ │ └── montajGetirFiltreli.py              # Assembly data with filters
│ ├── scripts/ # Utility scripts
│ │ └── generate_password_hash.py           # Password hash generator
│ ├── instance/                             # Database instance files
│ ├── venv/                                 # Python virtual environment
│ ├── app.py                                # Main Flask application
│ ├── main.py                               # Application entry point
│ ├── requirements.txt                      # Python dependencies
│ └── .env                                  # Environment configuration
│
├── frontend/                               # React Frontend
│ ├── build/                                # Production build files
│ ├── node_modules/                         # Node.js dependencies
│ ├── public/                               # Static assets (HTML, images, icons)
│ ├── src/                                  # React source code
│ │ ├── menu/                               # Navigation menu components
│ │ │ └── menu.jsx                          # Main menu component
│ │ ├── App.jsx                             # Root application component
│ │ ├── Dashboard.jsx                       # Dashboard page component
│ │ ├── index.css                           # Global stylesheet
│ │ ├── index.js                            # React DOM entry point
│ │ ├── Login.jsx                           # Authentication page
│ │ └── MontajIslemleri.jsx                 # Assembly operations page
│ ├── package-lock.json                     # Exact dependency versions
│ └── package.json                          # Node.js project configuration
│
├── screenshots/                            # screenshots
└── README.md # Project documentation
```
### 🔐 Password Management
## Generating Password Hashes
```bash
cd backend
venv\Scripts\activate
python scripts/generate_password_hash.py
```
### 🛠️ Development
## Running Both Servers
# From root directory
```bash
npm run dev
```
## Database Management
MySQL database configuration in .env file
Automatic table creation on first run
Data synchronization via UTTS APIs

## API Documentation
RESTful API endpoints
JSON request/response format
Error handling with status codes

# API Configuration (Get these from your UTTS Portal account)
UTTS_API_URL=https://api.utts.gov.tr
UTTS_API_KEY=your_personal_api_key_here

Note: For security reasons, actual API keys and database credentials are not included. You'll need to obtain your own credentials from the UTTS Portal.

## 👨‍💻 About the Project
This project was developed to address a specific business need from Beypet, who required a secure platform where technicians could access their individual installation data without visibility into other dealers' records.

The solution integrates with the UTTS API, synchronizes data to a local MySQL database, and provides a technician-specific dashboard through an intuitive React frontend.

## 📞 Contact
Merve Taş

GitHub: mervetas

Project Repository: https://github.com/mervetas/UTTS-BEYPET

## ⚠️ Usage Notice
This project is shared for learning and portfolio purposes.
Unauthorized commercial use, redistribution, or claiming ownership of this code is strictly prohibited.
If you find this useful, please provide proper credit to Merve Taş.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.