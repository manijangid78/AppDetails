from fastapi import FastAPI

app = FastAPI()

@app.get("/login")
async def home():
    return {
        "name":"Python",
        "framework":"FastApi"
    }

@app.get("/")
def read_root():
    return {"Hello": "World"}