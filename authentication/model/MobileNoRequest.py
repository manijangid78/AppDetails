from pydantic import BaseModel

class MobileNoRequest(BaseModel):
    mobile_no: str