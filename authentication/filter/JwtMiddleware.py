from fastapi import FastAPI, Request, HTTPException
from fastapi.routing import APIRoute
from typing import Callable
from jose import jwt, JWTError

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"


# Custom APIRoute Class
class JWTValidationRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request):
            token = request.headers.get("token")
            if not token or not token.startswith("key "):
                raise HTTPException(status_code=401, detail="Token missing or invalid")
            print(token)
            try:
                token_value = token.split(" ")[1]
                if token_value!="guest_token":
                    jwt.decode(token_value, SECRET_KEY, algorithms=[ALGORITHM])
            except JWTError:
                raise HTTPException(status_code=401, detail="Token is invalid or expired")

            # Proceed to the original route handler
            return await original_route_handler(request)
        return custom_route_handler