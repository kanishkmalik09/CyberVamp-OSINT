# 🧛 CyberVamp-OSINT

<p align="center">
  <b>A Lightweight Phone Number OSINT Intelligence Dashboard</b>
  <br>
  Investigate, validate, and retrieve publicly available phone number information.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" />
  <img src="https://img.shields.io/badge/OSINT-Open%20Source%20Intelligence-red" />
  <img src="https://img.shields.io/badge/Status-Development-orange" />
</p>

---

## 📌 Overview

**CyberVamp-OSINT** is a web-based Open Source Intelligence (OSINT) tool designed to perform phone number intelligence lookups.

Powered by the **NumVerify API**, the application validates phone numbers and retrieves useful metadata, including carrier information, country, geographical location, and line type.

The project provides a simple dashboard powered by Python Flask, making phone number intelligence accessible through a web interface.

## ✨ Features

- 📱 **Phone Number Validation** – Check whether a phone number is valid.
- 🌍 **Country Identification** – Retrieve the associated country and country code.
- 📡 **Carrier Detection** – Identify the telecom carrier when available.
- 📍 **Location Information** – Retrieve location metadata provided by the API.
- ☎️ **Line Type Detection** – Identify the reported phone line type.
- 🔄 **Multiple Number Formats** – Retrieve international and local formats.
- ⚡ **REST API Integration** – Backend communication through Flask.
- 🩺 **Health Check** – Check application status and API configuration.
- 🖥️ **Web Dashboard** – Access functionality through a browser-based interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-CORS | Cross-origin resource sharing |
| Requests | HTTP API communication |
| NumVerify API | Phone number intelligence |
| HTML/CSS/JavaScript | Frontend interface |

## 📂 Project Structure

```text
CyberVamp-OSINT/
│
├── templates/
│   └── index.html
│
├── app.py
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kanishkmalik09/CyberVamp-OSINT.git
```

### 2. Navigate to the project directory

```bash
cd CyberVamp-OSINT
```

### 3. Create a virtual environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask flask-cors requests
```

### 5. Configure NumVerify API

CyberVamp-OSINT requires a NumVerify API key.

Get your API key from:

https://numverify.com/

Set the API key as an environment variable.

**Windows (CMD)**

```bash
set NUMVERIFY_KEY=your_api_key_here
```

**Windows (PowerShell)**

```powershell
$env:NUMVERIFY_KEY="your_api_key_here"
```

**Linux / macOS**

```bash
export NUMVERIFY_KEY="your_api_key_here"
```

Replace `your_api_key_here` with your actual API key.

### 6. Run the application

```bash
python app.py
```

### 7. Access the dashboard

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

## 🔌 API Documentation

CyberVamp-OSINT provides REST API endpoints for interacting with the application.

### 1. Phone Number OSINT

**Endpoint:**

```http
POST /api/osint
```

**Request Body:**

```json
{
  "type": "phone",
  "value": "+14158586273"
}
```

**Example Response:**

```json
{
  "input": "+14158586273",
  "service": "NumVerify",
  "status": "success",
  "data": {
    "valid": true,
    "country": "United States",
    "country_code": "US",
    "carrier": "Example Carrier",
    "location": "California",
    "line_type": "mobile",
    "international_format": "+14158586273",
    "local_format": "4158586273"
  }
}
```

*Note: Response values depend on the actual API response. The example is illustrative.*

### 2. Application Health Check

**Endpoint:**

```http
GET /api/health
```

Returns application status and NumVerify configuration information.

**Example Response:**

```json
{
  "status": "online",
  "service": "NumVerify",
  "configured": true
}
```

## 🎯 Use Cases

- OSINT learning and research.
- Phone number format validation.
- Telecom carrier identification.
- Basic digital footprint investigations.
- Cybersecurity education and demonstrations.

## 🔐 Security & Responsible Usage

CyberVamp-OSINT is intended for educational, research, and legitimate cybersecurity purposes.

- Only investigate phone numbers when you have a lawful reason.
- Respect individual privacy and applicable data protection laws.
- Never use this tool for harassment, stalking, or unauthorized surveillance.
- Keep your API keys private.
- Do not commit API credentials to GitHub.
- Avoid exposing the development server to public networks.

**Security note:** The current implementation uses an HTTP NumVerify API endpoint and enables Flask debug mode. Do not deploy it publicly without securing API communications, disabling debug mode, and configuring an appropriate production server.

## 🚧 Future Enhancements

Potential improvements for future versions:

- [ ] Email OSINT lookup.
- [ ] Username intelligence gathering.
- [ ] IP address intelligence.
- [ ] Domain and DNS reconnaissance.
- [ ] Social media footprint analysis.
- [ ] Investigation history and report generation.
- [ ] Export results in JSON and PDF formats.
- [ ] Improved dashboard and visualization.
- [ ] Additional OSINT API integrations.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Submit a Pull Request.

## ⚠️ Disclaimer

This project is developed for educational purposes, cybersecurity research, and authorized OSINT investigations.

The developer is not responsible for any misuse of this software. Users are solely responsible for ensuring that their activities comply with applicable laws and regulations.

## 👨‍💻 Author

Kanishk Malik
Aditi Garg

GitHub: [@kanishkmalik09](https://github.com/kanishkmalik09)
         [@aditigarg-01](https://github.com/aditigarg-01)

Project: [CyberVamp-OSINT](https://github.com/kanishkmalik09/CyberVamp-OSINT)

---

<p align="center">
  <b>🧛 CyberVamp-OSINT — Explore Intelligence. Respect Privacy.</b>
</p>
