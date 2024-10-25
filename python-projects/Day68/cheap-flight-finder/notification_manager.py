import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import yagmail


class NotificationManager:

    def __init__(self):
        self.client = Client(
            os.environ['TWILIO_ACC_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.email = os.environ["gmail_user"]
        self.email_password = os.environ["gmail_app_password"]

    def send_sms(self, message_body):
        """
        Sends an WHATSAPP/SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS or WHATSAPP message from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        print(message.sid)

    def send_whatsapp(self, message_body):
        # See whatsappdocumentation here: https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        """
        Sends an email to a list of recipients using yagmail.
        """
        yag = yagmail.SMTP(user=self.email_user, password=self.email_password)
        subject = "New Low Price Flight!"

        for email in email_list:
            yag.send(
                to=email,
                subject=subject,
                contents=email_body
            )
        print("Emails sent successfully.")
