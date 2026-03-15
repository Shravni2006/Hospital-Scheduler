# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_reply
from flask import Flask, render_template, request, send_from_directory, url_for
from email_utils import send_confirmation_email
from sheets_helper import add_request_to_sheet
from pdf_utils import create_pdf_slip
import uuid
from datetime import datetime
import os

app = Flask(__name__)

SLIPS_FOLDER = os.path.join(os.getcwd(), "slips")

@app.route('/')
def home():
    return render_template('index.html')
# Doctor auto-assignment mapping
DOCTOR_MAP = {
    "Cardiology": {"doctor": "Dr. Mehta", "room": "Room 101"},
    "Neurology": {"doctor": "Dr. Sharma", "room": "Room 102"},
    "Orthopedics": {"doctor": "Dr. Patel", "room": "Room 103"},
    "Pediatrics": {"doctor": "Dr. Reddy", "room": "Room 104"},
    "ENT": {"doctor": "Dr. Iyer", "room": "Room 105"},
    "General": {"doctor": "Dr. Khan", "room": "Room 106"}
}


@app.route('/book', methods=['POST'])
def book_appointment():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    department = request.form['department']
    doctor_info = DOCTOR_MAP.get(department, {"doctor": "TBD", "room": "N/A"})
    doctor_name = doctor_info["doctor"]
    room_number = doctor_info["room"]

    preferred_date = request.form['date']
    preferred_time = request.form['time']

    request_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assigned_date = preferred_date
    assigned_time = preferred_time

    # save to Google Sheet
    add_request_to_sheet(
    request_id, timestamp, name, email, phone, department,
    preferred_date, preferred_time, assigned_date, assigned_time, "Confirmed", "", doctor_name
    )

    # generate PDF slip
    pdf_path = create_pdf_slip(request_id, name, department, assigned_date, assigned_time, email, phone, doctor_info=f"{doctor_name} ({room_number})")

    # send confirmation email with PDF
    send_confirmation_email(email, name, assigned_date, assigned_time, request_id, pdf_path=pdf_path)

    download_url = url_for('download_slip', filename=os.path.basename(pdf_path))
    return f"""
    <div style='text-align:center;margin-top:60px;font-family:Arial'>
      <h2 style='color:green;'>✅ Appointment Booked Successfully!</h2>
      <p><b>Request ID:</b> {request_id}</p>
      <p>Your appointment slip has been emailed to you and is available here:</p>
      <p><a href="{download_url}" style='font-size:16px;'>📄 Download Appointment Slip (PDF)</a></p>
      <p style='margin-top:20px;'><a href="/">← Book another appointment</a></p>
    </div>
    """

@app.route('/slips/<path:filename>')
def download_slip(filename):
    return send_from_directory(SLIPS_FOLDER, filename, as_attachment=True)
# 💬 Chatbot routes
@app.route('/chat')
def chat_page():
    return render_template('chatbot.html')

@app.route('/chatbot', methods=['POST'])
def chatbot_reply():
    data = request.get_json()
    user_message = data.get("message", "")
    from chatbot import get_chatbot_reply  # import inside to avoid circular import
    reply = get_chatbot_reply(user_message)
    return jsonify({"reply": reply})
@app.route('/verify')
def verify_qr():
    request_id = request.args.get('id')
    from sheets_helper import get_request_by_id
    data = get_request_by_id(request_id)
    if not data:
        return "<h3 style='color:red;text-align:center;'>❌ Invalid or expired QR code.</h3>"
    return f"""
    <div style='font-family:Arial;text-align:center;margin-top:50px'>
      <h2>✅ Appointment Verified</h2>
      <p><b>Name:</b> {data['Name']}</p>
      <p><b>Department:</b> {data['Department']}</p>
      <p><b>Date:</b> {data['AssignedDate']}</p>
      <p><b>Time:</b> {data['AssignedTime']}</p>
      <p><b>Request ID:</b> {request_id}</p>
      <p style='color:green;'>✔ This appointment is valid.</p>
    </div>
    """



if __name__ == "__main__":
    app.run(debug=True)


