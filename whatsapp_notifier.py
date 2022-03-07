from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
SENDER = os.environ.get('TWILIO_FROM_NUMBER')
TO = os.environ.get('TWILIO_TO_NUMBER')

class WhatsappMessageSender:

    def __init__(self, message):
        self.message_to_send = message
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN) 


    def send_message(self):
        message = self.client.messages.create( 
                              from_=SENDER,  
                              body=self.message_to_send,      
                              to=TO,
                          )
        print("Message sent successfully")

# test_message_sender = WhatsappMessageSender("Testing the class")
# test_message_sender.send_message() 