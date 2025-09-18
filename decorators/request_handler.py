from functools import wraps
from starlette.responses import JSONResponse
from models.resp.base import Resp
import json

def handle_request(func):
    @wraps(func)
    async def wrapper(request):
        try:
            response = await func(request)
            if response and response.body:
                return JSONResponse(
                    status_code=200,
                    content=Resp(code=0, data=json.loads(response.body.decode("utf-8")), message="success").model_dump(),
                )
            return JSONResponse(
                    status_code=200,
                    content=Resp(code=0, data=None, message="success").model_dump(),
                )
        except Exception as e:
            return JSONResponse(
                status_code=200,
                content=Resp(code=-1, data=None, message=str(e)).model_dump(),
            )
    return wrapper

