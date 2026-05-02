# 🛡️ PhishGuard India – Scam Detection System

## 📌 Project Overview

PhishGuard India is an AI-inspired scam detection web application developed to identify suspicious messages, phishing URLs, and scam-related content. The system analyzes user-provided text and links using keyword analysis and URL validation techniques to classify the input as **Safe**, **Suspicious**, or **Scam**.

This project is designed for educational purposes and cybersecurity awareness, helping users detect common phishing attempts, fake messages, and malicious URLs.

---

# 🚀 Features

* 🔍 Scam keyword detection
* 🌐 Suspicious URL analysis
* ⚠️ Detection of phishing indicators
* 🔒 HTTPS verification
* 🎯 Scam scoring mechanism
* 💻 FastAPI backend integration
* 🎨 Modern cyber-themed frontend UI
* 📊 Real-time scam analysis results

---

# 🛠️ Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* FastAPI

## Libraries

* Uvicorn
* Validators
* TLDExtract
* Jinja2
* Pydantic

---

# 📂 Project Structure

```bash
Scam_detector/
│
├── main.py
├── scorer.py
├── text_checker.py
├── url_checker.py
├── requirements.txt
│
└── frontend/
    └── index.html
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Scam_detector.git
```

## 2️⃣ Navigate to Project Folder

```bash
cd Scam_detector
```

## 3️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / WSL

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python -m uvicorn main:app --reload
```

---

# 🌐 Open in Browser

```bash
http://127.0.0.1:8000
```

---

# 🧪 Example Test Input

```text
Urgent! Your bank account will be blocked. Verify your OTP now.
```

---

# 📊 Example Output

```json
{
  "result": "Scam",
  "confidence": 100
}
```

---

# 🔐 Scam Detection Techniques Used

* Scam keyword matching
* URL validation
* HTTPS verification
* Suspicious domain extension detection
* Shortened URL detection

---

# 🎯 Future Enhancements

* Machine Learning based detection
* Email attachment scanning
* Real-time browser extension
* QR code phishing detection
* Database integration
* User authentication system
* Threat intelligence integration

---

# 👨‍💻 Author

**Shreyash Ashok Deore**
Computer Engineering Student
Cybersecurity Enthusiast

---

# ⭐ GitHub Repository

If you like this project, give it a ⭐ on GitHub.

---

# 📜 License

This project is developed for educational and learning purposes.
