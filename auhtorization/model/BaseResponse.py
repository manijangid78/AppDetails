from typing import Any, Union
from pydantic import BaseModel

from authentication.model.JwtToken import JwtToken
from authentication.model.OTPDto import OTPDto


class BaseResponse(BaseModel):
    status: str
    message: str
    data: Union[Any]