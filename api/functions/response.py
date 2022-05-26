# Copyright (c) 2022 Itz-fork

from fastapi.responses import JSONResponse


async def send_response(data, code = 200):
    """
    Return a Json Response

    ### Arguments:

        - `data` - Content to send as a response
        - `code` - HTTP status code (if data is empty, status code will be re-assigned as 404. Defaults to 200)
    """
    resp = {}
    code = 404 if not data else code
    resp["status"] = "ok" if code == 200 else "bad"
    resp["data"] = data if data else ""
    return JSONResponse(
        content=resp,
        status_code=code
    )