# pdf_utils.py
import os
from fpdf import FPDF
import qrcode
from PIL import Image

SAVEPATH = "slips"

def ensure_dir():
    if not os.path.exists(SAVEPATH):
        os.makedirs(SAVEPATH)

def generate_qr(data_str, qr_path):
    # create and save QR code image
    qr = qrcode.QRCode(box_size=6, border=2)
    qr.add_data(data_str)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)
    return qr_path

def create_pdf_slip(request_id, name, department, assigned_date, assigned_time, email, phone, doctor_info="TBD"):
    """
    Creates a PDF slip file and returns its path.
    File name: slips/<request_id>_slip.pdf
    """
    ensure_dir()
    filename = f"{request_id}_slip.pdf"
    file_path = os.path.join(SAVEPATH, filename)

    # QR contains essential details (you can customize)
    qr_text = f"http://127.0.0.1:5000/verify?id={request_id}"

    qr_img_path = os.path.join(SAVEPATH, f"{request_id}_qr.png")
    generate_qr(qr_text, qr_img_path)

    # Create PDF using FPDF
    pdf = FPDF(format='A4')  # small slip size, change as needed
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=5)

    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Hospital Appointment Slip", ln=True, align="C")
    pdf.ln(4)

    # Details
    pdf.set_font("Arial", size=11)
    pdf.cell(45, 6, f"Request ID: ", ln=0)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0,6, request_id, ln=1)

    pdf.set_font("Arial", size=11)
    pdf.cell(45, 6, "Name: ", ln=0)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0,6, name, ln=1)

    pdf.set_font("Arial", size=11)
    pdf.cell(45, 6, "Department: ", ln=0)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0,6, department, ln=1)

    pdf.set_font("Arial", size=11)
    pdf.cell(45, 6, "Doctor: ", ln=0)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0,6, doctor_info, ln=1)

    pdf.set_font("Arial", size=11)
    pdf.cell(45, 6, "Date: ", ln=0)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0,6, assigned_date, ln=1)

    pdf.set_font("Arial", size=11)
    pdf.cell(45, 6, "Time: ", ln=0)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0,6, assigned_time, ln=1)

    pdf.ln(4)
    pdf.set_font("Arial", size=9)
    pdf.multi_cell(0, 5, "Please arrive 10 minutes early and carry a government ID. Show this slip at reception.")

    # Insert QR image on the right (absolute position)
    if os.path.exists(qr_img_path):
        # ensure the QR fits: x, y, w (in mm)
        pdf.image(qr_img_path, x=120, y=20, w=35)

    # Save PDF
    pdf.output(file_path)

    # Optionally remove the QR PNG (comment out if you want to keep)
    try:
        os.remove(qr_img_path)
    except:
        pass

    return file_path
