import smtplib
import datetime as dt
import os
from dotenv import load_dotenv

# Loading the variables into the current environment
load_dotenv()

# Storing the environment variables
FROM_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('MY_PASSWORD')
TO_EMAIL = os.environ.get('TO_EMAIL')

class EmailSender:

    def __init__(self, message_to_send):
        self.message = message_to_send

    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg=f"Subject: Weather Summary ahead of spraying day\n\n{self.message}".encode("utf-8"))

# test_email_sender = EmailSender("Message to be sent will be here")
# test_email_sender.send_email()