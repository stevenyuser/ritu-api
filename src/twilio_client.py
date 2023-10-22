from twilio import twiml
from twilio.rest import Client

PHONE_NUMBER = "+18555345790"
# APP_SID= "APc62df12923f706674be1859f51f2052e"

TOKEN = "9cddb442808bbdc2547b65f81da59df3"
SID = "AC873a9461e836be4436b3823ad5e58238"

def sendMessage(body, number):
    client = Client(SID, TOKEN)
    client.messages.create(to=number, from_=PHONE_NUMBER, body=body)

