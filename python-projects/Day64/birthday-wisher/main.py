# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import yagmail
from dotenv import load_dotenv
from datetime import datetime
import pandas
import random
import smtplib
import os
load_dotenv(override=True)

gmail_user = os.environ['gmail_user']
gmail_password = os.environ['gmail_app_password']

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        print(f"Email content before replacement: \n{contents}")
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(f"Email content after replacement: \n{contents}")

    email = yagmail.SMTP(user=gmail_user,
                         password=gmail_password)
    email.send(
        to=birthday_person['email'],
        subject=f"Happy Birthday!\n\n",
        contents=contents
    )
