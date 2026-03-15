import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

# Google Sheets authentication
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
SHEET_KEY = os.getenv("SHEET_KEY")

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_KEY).sheet1

def add_request_to_sheet(request_id, timestamp, name, email, phone, department,
                         preferred_date, preferred_time, assigned_date, assigned_time, status, notes, doctor_name):
    sheet.append_row([request_id, timestamp, name, email, phone, department,
                      preferred_date, preferred_time, assigned_date, assigned_time, status, notes, doctor_name])

    """
    Adds a new appointment row to the Google Sheet
    Columns: RequestID | Timestamp | Name | Email | Phone | Department | PreferredDate | PreferredTime | AssignedDate | AssignedTime | Status | Notes
    """
    row = [
        request_id, timestamp, name, email, phone, department,
        preferred_date, preferred_time, assigned_date, assigned_time, status, notes
    ]
    sheet.append_row(row, value_input_option="USER_ENTERED")
    def get_request_by_id(request_id):
     records = sheet.get_all_records()
     for row in records:
        if str(row['RequestID']) == str(request_id):
            return row
    return None

