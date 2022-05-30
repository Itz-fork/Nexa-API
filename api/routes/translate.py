# Copyright (c) 2022 - Itz-fork

from fastapi import APIRouter

from ..functions.http_req import fetch
from ..functions.response import send_response
from ..models.Languages import TranslateModel

route = APIRouter()

@route.get(
    "/tr",
    description="Translate text using google translate",
    response_model=TranslateModel,
    tags=["Language"])
async def google_translate(text: str, dest: str = "en"):
    tr = (await fetch(f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl={dest}&q={text}"))[0]
    res = {}
    res["translation"] = tr[0]
    res["origin"] = tr[1]
    res["dest"] = dest
    return await send_response(res)