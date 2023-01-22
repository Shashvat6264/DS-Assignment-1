from fastapi import FastAPI
from .controllers import *

from .system import *

app = FastAPI()

@app.get("/health", tags=["HEALTH"])
async def health():
    return {"message": "Server Running Successfully..."}