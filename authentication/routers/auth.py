from fastapi import APIRouter, Request

from authentication.filter.JwtMiddleware import JWTValidationRoute
from authentication.model.BaseResponse import BaseResponse
from authentication.model.MobileNoRequest import MobileNoRequest
from authentication.model.OTPDto import OTPDto
from authentication.service.JWTService import JwtService
from authentication.service.AuthService import AuthService

router = APIRouter(route_class=JWTValidationRoute)

list_of_mobile_no = {"7822917942":"","9999999999":""}

@router.get("/")
def helloApi():
    return {
        "message":"hello, lets start"
    }

@router.post("/verifyMobile",response_model= BaseResponse)
def verifyMobileNo(request:Request, mobile_req: MobileNoRequest):
    token_value = checkGuestToken(request.headers.get("token"))
    if token_value==1:
        otp_dto = AuthService.verifyMobile(mobile_req)
        if otp_dto is None:
            return BaseResponse(
                status="failure",
                message="mobile verification failed",
                data=None
            )
        else:
            return BaseResponse(
                status="success",
                message="mobile verified successfully",
                data=otp_dto
            )
    else:
        return BaseResponse(
            status="failure",
            message="token verification failed",
            data=None
        )

@router.post("/verifyOTP", response_model=BaseResponse)
def verifyOTP(request:Request, otp_dto: OTPDto):
    token_value = checkGuestToken(request.headers.get("token"))
    if token_value==1:
        otp_send = AuthService.verifyOtp(otp_dto, request.headers.get("deviceId"))
        if isinstance(otp_send, int):
            if otp_send == 1:
                return BaseResponse(
                    status="failure",
                    message="mobile verified failed",
                    data=None
                )
            else:
                return BaseResponse(
                    status="failure",
                    message="otp verified failed",
                    data=None
                )
        else:
            return BaseResponse(
                status="success",
                message="mobile verified success",
                data=otp_send
            )
    else:
        return BaseResponse(
            status="failure",
            message="token verification failed",
            data=None
        )

@router.post("/resendOtp", response_model=BaseResponse)
def resendToken(request:Request,  mobile_req: MobileNoRequest):
    otp_dto = AuthService.verifyMobile(mobile_req)
    if otp_dto is None:
        return BaseResponse(
            status="failure",
            message="mobile verification failed",
            data=None
        )
    else:
        return BaseResponse(
            status="success",
            message="mobile verified successfully",
            data=otp_dto
        )

@router.post("/verifyToken", response_model=BaseResponse)
def verifyToken(request: Request):
    token = request.headers.get("token").removeprefix("key ")
    return BaseResponse(
        status="success",
        message="token verified successfully",
        data=JwtService.verifyToken(token)
    )

# @router.post("/revokeToken", response_model=BaseResponse)
# def revokeToken(request:Request):
#     AuthService

def checkGuestToken(token:str):
    token = token.removeprefix("key ")
    if token == "guest_token":
        return 1
    else:
        return 0