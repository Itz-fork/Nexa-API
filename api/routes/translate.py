# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from ..functions.http_req import fetch
from ..functions.response import send_response

route = APIRouter()

@route.get("/tr", description="Translate text using google translate", tags=["Language"])
async def google_translate(text: str, dest: str = "en"):
    tr = await fetch(f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl={dest}&q={text}")
    return await send_response(tr)