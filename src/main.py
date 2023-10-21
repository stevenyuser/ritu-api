from fastapi import FastAPI, Form, Response
from src.firebase.auth import start_firebase

from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()
db = start_firebase()


@app.get("/ping", status_code=200)
async def ping():
    return {"message": "pong"}

@app.get("/paul", status_code=200)
async def paul():
    return {"message": db.collection('users').document('1').get().to_dict()}


@app.post("/sms")
async def sms(From: str = Form(...), Body: str = Form(...)):
    response = MessagingResponse()
    msg = response.message(f"Hi {From}, you said: {Body}")
    return Response(content=str(response), media_type="application/xml")
