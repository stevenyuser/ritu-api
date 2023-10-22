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


from src.api.db_user_lookup import get_user_by_number

# sms route - texting to the phone number sends a request to the "/sms" route
@app.post("/sms")
async def sms(From: str = Form(...), Body: str = Form(...)):
    # From: the phone number, Body: the text message itself

    # response = MessagingResponse()
    # msg = response.message(f"Hi {From}, you said: {Body}")
    # return Response(content=str(response), media_type="application/xml")

    response = MessagingResponse()
    number = From
    text = Body

    coords_time_dict = get_user_by_number(db, number=number)

    # message = algo(coords_time_dict)

    if coords_time_dict is None:
        print(f"No user accounts with {number}!")

    msg = response.message(f"Hi {number}, you sent this text: {text}")
    print(msg)
    return Response(content=str(response), media_type="application/xml")

from src.twilio_client import sendMessage
from src.models.send_sms_model import Send_SMS_Request

@app.post("/send_sms")
async def send_sms(request: Send_SMS_Request):
    sendMessage("testing!", request.phone_number) # replace later
    return {"message": "success"}