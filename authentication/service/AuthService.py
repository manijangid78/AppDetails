import random

from authentication.model.JwtToken import JwtToken
from authentication.model.MobileNoRequest import MobileNoRequest
from authentication.model.OTPDto import OTPDto
from authentication.service.JWTService import JwtService

list_of_mobile_no = {"7822917942":"","9999999999":""}
blocklist = set()


def generateToken(device_id: str):
    return JwtToken(
        token=JwtService.generateToken(device_id)
    )

class AuthService:

    def verifyMobile(self:MobileNoRequest):
        if self.mobile_no in list_of_mobile_no:
            otp = random.randint(111111, 999999)
            list_of_mobile_no[self.mobile_no]=otp
            return OTPDto(
                mobile_no=self.mobile_no,
                otp= otp
            )
        else:
            return None

    def verifyOtp(otp_dto:OTPDto,device_id:str):
        if otp_dto.mobile_no in list_of_mobile_no:
            print(list_of_mobile_no)
            if otp_dto.otp == list_of_mobile_no.get(otp_dto.mobile_no):
                print(device_id)
                return generateToken(device_id)
            else:
                return 2
        else:
            return 1



    def revokeToken(self, token:str):


        return 1



