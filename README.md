# 🏥 Smart Hospital Appointment Scheduler

A **web-based hospital appointment automation system** built using **Python, Flask, Google Sheets API, Email Automation, PDF generation, and QR verification**.

This project demonstrates how **Robotic Process Automation (RPA)** and web technologies can streamline hospital appointment workflows — from booking to confirmation and verification.

---

## 🚀 Features

- 🧾 Online appointment booking system
- 🤖 Automated scheduling workflow
- 👨‍⚕️ Doctor auto-assignment based on department
- 📧 Email confirmation to patients
- 📄 Automatic PDF appointment slip generation
- 📱 QR code verification for appointments
- 📊 Google Sheets used as a lightweight database
- 💬 Chatbot assistant for patient queries
- ⏰ Reminder automation for upcoming appointments
- 🔍 Appointment verification via QR scan

---

## 🧠 System Workflow

```
Patient → Web Form (Flask)
            │
            ▼
   Appointment Processing
            │
            ▼
     Google Sheets Database
            │
   ┌────────┼────────┐
   ▼                 ▼
Email Confirmation   PDF Slip + QR Code
   │
   ▼
 Patient Receives Appointment
```

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Automation
- RPA Concepts
- UiPath Integration (optional)

### Database
- Google Sheets API

### Libraries
- Flask
- gspread
- oauth2client
- FPDF
- Pillow
- qrcode
- python-dotenv

---

## 📂 Project Structure

```
hospital_scheduler/
│
├── app.py
├── sheets_helper.py
├── email_utils.py
├── pdf_utils.py
├── chatbot.py
├── reminder_scheduler.py
│
├── templates/
│   ├── index.html
│   └── chatbot.html
│
├── slips/
│
├── service_account.json
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/hospital_scheduler.git
cd hospital_scheduler
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or manually

```bash
pip install flask gspread oauth2client fpdf pillow qrcode python-dotenv
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```
SENDER_EMAIL=your_email@gmail.com
EMAIL_APP_PASSWORD=your_app_password
SERVICE_ACCOUNT_FILE=service_account.json
SHEET_KEY=your_google_sheet_key
```

---

### 5. Run the Application

```bash
python app.py
```

Open the browser:

```
http://127.0.0.1:5000
```

---

## 📸 Example Workflow

1. Patient fills appointment form
2. System stores data in Google Sheets
3. Doctor automatically assigned
4. Confirmation email sent
5. PDF slip generated
6. QR code added to slip
7. Patient scans QR at hospital reception

---

## 🤖 RPA Integration (UiPath)

This project can also integrate with **UiPath automation workflows** for:

- Automated hospital reporting
- Patient reminder automation
- Data synchronization with hospital ERP systems
- Email workflow automation

---

## 🔒 Security

- Google Service Account authentication
- Environment variables for credentials
- QR verification for appointment validation

---

## 💡 Future Improvements

- Payment gateway integration
- SMS notifications
- Doctor dashboard
- AI chatbot for medical queries
- Hospital admin analytics dashboard
- Mobile app integration

---

## 👩‍💻 Author

**Shravni Andhale**

Computer Science Student  
Interested in **Automation, AI, and Full Stack Development**

---

## ⭐ Support

If you like this project:

- Star ⭐ the repository
- Fork 🍴 the project
- Submit pull requests

---

## 📜 License

This project is licensed under the **MIT License**.
