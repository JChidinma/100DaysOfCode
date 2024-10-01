import random
import string
import webbrowser
from fpdf import FPDF
import os


class Ticket:
    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.ticket_id = "".join(
            [random.choice(string.ascii_letters) for i in range(8)])
        self.seat_number = seat_number

    def save_ticket_to_pdf(self):
        # path = f"/path"
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Your Digital Ticket",
                 border=0, align="C", ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Name: ", border=1)
        pdf.set_font(family='Times', size=12, style='')
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Ticket ID ", border=1)
        pdf.set_font(family='Times', size=12, style='')
        pdf.cell(w=0, h=25, txt=self.ticket_id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family='Times', size=12, style='')
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Seat Number", border=1)
        pdf.set_font(family='Times', size=12, style='')
        pdf.cell(w=0, h=25, txt=str(self.seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        # pdf.output("files/ticket_report.pdf", 'F')
        filename = f"{self.ticket_id}_ticket_report.pdf"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

            filepath = os.path.join(output_dir, filename)
            pdf.output(filepath)
            webbrowser.open(self.filename)
