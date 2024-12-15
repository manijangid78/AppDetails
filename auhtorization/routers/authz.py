from fastapi import APIRouter, Request

from auhtorization.model.BaseResponse import BaseResponse

router = APIRouter()

@router.post("/getToken", response_model=BaseResponse)
def getToken(request:Request):

    return ""