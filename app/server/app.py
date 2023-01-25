from fastapi import FastAPI
from .controllers import *

app = FastAPI()

from .exceptions import *
from .routers import router

from .system import *

app.include_router(router, prefix="")

@app.get("/health", tags=["HEALTH"])
async def health():
    return {"message": "Server Running Successfully..."}