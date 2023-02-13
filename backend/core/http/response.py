from fastapi.responses import JSONResponse
import json

default_headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'access-control-allow-credentials': 'false',
}

def success_response(data="ok"):
    return JSONResponse(
        headers=dict(default_headers), 
        content=data, 
        status_code=200
    )