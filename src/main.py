from fastapi import FastAPI, Request
from src.firebase.auth import start_firebase

app = FastAPI()
db = start_firebase()


@app.get("/ping", status_code=200)
async def ping():
    return {"message": "pong"}

@app.get("/paul", status_code=200)
async def paul():
    return {"message": db.collection('users').document('1').get().to_dict()}