import os
import random
import pandas
from dotenv import load_dotenv
from datetime import datetime
from twilio.rest import Client

load_dotenv(override=True)

account_sid = os.environ['TWILIO_ACC_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
# Twilio sandbox WhatsApp number
twilio_whatsapp_number = "whatsapp:my_twilio_sandbox_number"

recipient_whatsapp_number = "whatsapp:recipient_number"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today matches any birthday in the CSV
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send the birthday message to WhatsApp using Twilio
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=contents,
        from_=twilio_whatsapp_number,
        to=recipient_whatsapp_number
    )

    print(
        f"WhatsApp message sent to {birthday_person['name']} at {recipient_whatsapp_number}. Status: {message.status}")
else:
    print("No birthdays today.")
