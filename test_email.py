import os, smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

SENDER = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

msg = EmailMessage()
msg["From"] = SENDER
msg["To"] = SENDER
msg["Subject"] = "Test Email from Hospital Scheduler"
msg.set_content("Hi Shravni! ✅ This is a test email sent via Python Gmail SMTP!")

# Connect to Gmail and send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(SENDER, PASSWORD)
    smtp.send_message(msg)

print("✅ Email sent successfully!")
