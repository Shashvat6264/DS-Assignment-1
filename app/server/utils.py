from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def generic_Response(data, status_code):
    response = jsonable_encoder(data)
    return JSONResponse(response, status_code=status_code)