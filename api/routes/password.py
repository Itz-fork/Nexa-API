# Copyright (c) 2022 Itz-fork

from random import sample
from fastapi import APIRouter
from string import punctuation
from secrets import token_urlsafe
from ..functions.response import send_response

route = APIRouter()

@route.get("/password", description="Generates a random password according to the given length")
async def password(length: int = 12):
    tkn = token_urlsafe(length)
    punc = "".join(sample(punctuation, 1))
    return await send_response("".join(sample(f"{tkn+punc}", length)))