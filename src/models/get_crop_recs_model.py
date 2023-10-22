from pydantic import BaseModel

class Get_Crop_Recs_Request(BaseModel):
    phone_number: str