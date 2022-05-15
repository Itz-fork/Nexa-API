# Copyright (c) 2022 Itz-fork

from random import sample
from fastapi import APIRouter
from string import punctuation
from secrets import token_urlsafe

from ..functions.response import send_response
from ..config.basic import NX_Basic

route = APIRouter()


@route.get("/password", description="Generates a random password according to the given length", tags=["Tools"])
async def password_generator(length: int = 12):
    if length > NX_Basic["pass_limit"]:
        return await send_response(500, [])
    tkn = token_urlsafe(length)
    punc = "".join(sample(punctuation, 1))
    return await send_response("".join(sample(f"{tkn+punc}", length)))
