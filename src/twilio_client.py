from twilio import twiml
from twilio.rest import Client
import os

PHONE_NUMBER = "+18555345790"
# APP_SID= os.environ["TWILIO_APP_SID"]

TOKEN = os.environ["TWILIO_TOKEN"]
SID = os.environ["TWILIO_SID"]

def sendMessage(body, number):
    client = Client(SID, TOKEN)
    client.messages.create(to=number, from_=PHONE_NUMBER, body=body)

