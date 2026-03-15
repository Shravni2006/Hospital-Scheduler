from google.oauth2.service_account import Credentials
import gspread

SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_file("service_account.json", scopes=SCOPES)
gc = gspread.authorize(creds)

sh = gc.open_by_key("b662881a4a69c482a0ff07a11c54d4a8566a5580")
print("Sheet title:", sh.sheet1.title)
