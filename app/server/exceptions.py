from fastapi import Request, status
from fastapi.responses import JSONResponse
from .app import app
from .controllers import *


@app.exception_handler(UnauthorizedException)
async def unauthorized_exception_handler(request: Request, error: UnauthorizedException):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "status": "failure",
            "message": f"{str(error)}"
        },
    )
    
@app.exception_handler(TopicDoesNotExist)
async def topicdoesnotexist_exception_handler(request: Request, error: TopicDoesNotExist):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status": "failure",
            "message": f"{str(error)}"
        },
    )