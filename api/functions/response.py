# Copyright (c) 2022 Itz-fork
from fastapi.responses import JSONResponse

async def send_response(data, code = 200):
    resp = {}
    resp["status"] = "ok"
    resp["data"] = data
    return JSONResponse(
        content=resp,
        status_code=code
    )