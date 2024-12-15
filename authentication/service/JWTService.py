import jwt
import datetime

# Secret key for encoding
SECRET_KEY = "your_secret_key"

class JwtService:
    def generateToken(deviceId: str):
        # Data to encode
        payload = {
            "user_id": 123,
            "username": "john_doe",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Token expiry
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        print("Generated JWT Token: {}",token)
        return token

    def verifyToken(token:str):
        try:
            decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return "Decoded Data {}",decoded_data
        except jwt.ExpiredSignatureError:
            return "Token has expired"
        except jwt.InvalidTokenError:
            return "Invalid token"