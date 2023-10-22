from pydantic import BaseModel

class Send_SMS_Request(BaseModel):
    phone_number: str
