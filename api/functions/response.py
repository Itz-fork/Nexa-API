# Copyright (c) 2022 Itz-fork

async def send_response(data):
    resp = {}
    resp["status"] = "ok"
    resp["data"] = data
    return resp