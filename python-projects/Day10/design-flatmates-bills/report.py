import webbrowser
from fpdf import FPDF
import os


class PdfReport:
    """
    Creates a PDF file that contains a report of the flatmates names, period they stayed in the house and their paid amount
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.amount_paid(
            bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.amount_paid(
            bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image(
            "files/house.png", w=30, h=30)

        # Add fonts
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=100, h=25, txt="Period", border=0)
        pdf.cell(w=150, h=25, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # pdf.output("flatmate_bill_report.pdf")
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
