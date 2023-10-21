from twilio import twiml

PHONE_NUMBER = "+18555345790"
APP_SID= "APc62df12923f706674be1859f51f2052e"

TOKEN = "AC873a9461e836be4436b3823ad5e58238"
SID = "63155ab5ce90bb3b32a8cedb9249a705"

def sendMessage(body, number):
    client = Client(SID, TOKEN)
    client.messages.create(to=number, from_=PHONE_NUMBER, body=body, messaging_service_sid=APP_SID)

