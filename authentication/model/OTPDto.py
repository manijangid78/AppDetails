from pydantic import BaseModel

class OTPDto(BaseModel):
    mobile_no: str
    otp: int