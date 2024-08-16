from flat import Bill, Flatmate
from report import PdfReport
from try_filestack import FileSharer


amount = float(input("How much is your flat's total bill in $:\n"))
period = input("Enter the bill's period. E.g. August 2024: \n")

name1 = input(("What is your name?\n"))
days_in_house1 = int(
    input(f"How many days did {name1} spend in the house during the bill period?\n"))

name2 = input("What is your flatmate's name?\n")
days_in_house2 = int(
    input(f"How many days did {name2} spend in the house during the bill period?\n"))


bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1} pays: ", flatmate1.amount_paid(bill, flatmate2))
print(f"{flatmate2} pays: ", flatmate2.amount_paid(bill, flatmate1))

pdf_report = PdfReport(filename=f"{period}_bill.pdf")
pdf_report.generate(flatmate1, flatmate2, bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
