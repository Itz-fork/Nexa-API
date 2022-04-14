# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from py_trans import Async_PyTranslator
from ..functions.response import send_response

route = APIRouter()

@route.get("/tr")
async def translate(text: str, dest: str = "en"):
    t = Async_PyTranslator()
    tr = await t.translate(text, dest)
    return await send_response(tr)