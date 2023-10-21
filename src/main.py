# config and imports
from fastapi import FastAPI, Form, Response
from src.firebase.auth import start_firebase

from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse

# Create the App Instances
app = FastAPI()
db = start_firebase()

# test methods

@app.get("/ping", status_code=200)
async def ping():
    return {"message": "pong"}

# testing firebase firestore
@app.get("/firestore", status_code=200)
async def paul():
    return {"message": db.collection('users').document('1').get().to_dict()}

# sms route - texting to the phone number sends a request to the "/sms" route
@app.post("/sms")
async def sms(From: str = Form(...), Body: str = Form(...)):
    # From: the phone number, Body: the text message itself

    # response = MessagingResponse()
    # msg = response.message(f"Hi {From}, you said: {Body}")
    # return Response(content=str(response), media_type="application/xml")

    response = MessagingResponse()
    sender = From
    text = Body
    msg = response.message(f"Hi {sender}, you sent this text: {text}")
    print(msg)
    return Response(content=str(response), media_type="application/xml")
