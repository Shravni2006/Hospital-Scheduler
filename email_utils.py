# email_utils.py
import os, smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import mimetypes

load_dotenv()

SENDER = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

def send_confirmation_email(to_email, name, assigned_date, assigned_time, request_id, pdf_path=None):
    subject = f"Appointment Confirmed: {assigned_date} {assigned_time}"
    body = f"""Hello {name},

Your hospital appointment has been successfully confirmed.

Date: {assigned_date}
Time: {assigned_time}
Request ID: {request_id}

Attached is your appointment slip (PDF). Please show it at the reception.

Best regards,
Hospital Appointment Scheduler Bot
"""
    msg = EmailMessage()
    msg["From"] = SENDER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    # attach PDF if available
    if pdf_path and os.path.exists(pdf_path):
        mime_type, _ = mimetypes.guess_type(pdf_path)
        if mime_type is None:
            mime_type = "application/octet-stream"
        maintype, subtype = mime_type.split("/", 1)
        with open(pdf_path, "rb") as f:
            msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(pdf_path))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER, PASSWORD)
        smtp.send_message(msg)
