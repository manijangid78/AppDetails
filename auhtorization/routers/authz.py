from fastapi import APIRouter, Request

from auhtorization.model.BaseResponse import BaseResponse
from auhtorization.service.JWTService import JwtService
from auhtorization.model.JwtToken import JwtToken

router = APIRouter()

@router.post("/getToken", response_model=BaseResponse)
def getToken(request:Request):
    token = JwtService.generateToken(request.headers.get("deviceId"))
    jwtToken = JwtToken(token = token)
    return BaseResponse(
        status="success",
        message="token generated successfully",
        data=jwtToken
    )

@router.get("/verifyToken", response_model=BaseResponse)
def verifyToken(request: Request):
    data = JwtService.verifyToken(request.headers.get("token").removeprefix("key "))
    if isinstance(data, int):
        if data ==1:
            return BaseResponse(
                status="failure",
                message="Token has expired",
                data=None
            )
        elif data==2:
            return BaseResponse(
                status="failure",
                message="Invalid token",
                data=None
            )
    else:
        return BaseResponse(
            status="success",
            message="Token verified successfully",
            data=data
        )

