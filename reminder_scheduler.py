# reminder_scheduler.py
import datetime
import time
import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
from email_utils import send_confirmation_email

load_dotenv()

# Connect to Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
SHEET_KEY = os.getenv("SHEET_KEY")

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_KEY).sheet1

def send_reminders():
    print("⏰ Checking for appointments to remind...")
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    data = sheet.get_all_records()
    for row in data:
        assigned_date = row.get("AssignedDate")
        status = row.get("Status")
        if not assigned_date or status != "Confirmed":
            continue

        # Convert to date object for comparison
        try:
            appt_date = datetime.datetime.strptime(assigned_date, "%Y-%m-%d").date()
        except:
            continue

        # If appointment is tomorrow, send reminder
        if appt_date == today:
            name = row.get("Name")
            email = row.get("Email")
            assigned_time = row.get("AssignedTime")
            request_id = row.get("RequestID")

            msg = f"Hello {name},\n\nThis is a reminder that your hospital appointment is scheduled for tomorrow at {assigned_time}.\n\nRequest ID: {request_id}\n\nPlease arrive 10 minutes early.\n\n- Hospital Appointment Scheduler"
            print(f"📩 Sending reminder to {name} ({email}) for {assigned_time}")

            # reuse send_confirmation_email but with custom message
            send_confirmation_email(email, name, str(tomorrow), assigned_time, request_id)

# For continuous background run
if __name__ == "__main__":
    print("🚀 Reminder Scheduler started...")
    while True:
        current_time = datetime.datetime.now().time()
        # Run daily at 08:00 AM
        if current_time.hour == 8 and current_time.minute == 0:
            send_reminders()
            print("✅ All reminders sent!")
            time.sleep(60)  # wait a minute to avoid double sending
        time.sleep(30)
