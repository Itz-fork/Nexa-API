# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from PyDictionary import PyDictionary
from functools import partial
from asyncio import get_running_loop

from ..functions.response import send_response


route = APIRouter()


def define(word):
    dic = PyDictionary()
    mn = dic.meaning(word)
    result = {}
    if type(mn) is dict:
        # Iterate through key value pairs of the dict (not dick)
        for k, v in mn.items():
            result["type"] = k
            result["definition"] = v
    return result

@route.get("/define", description="Get the definition of a word", tags=["Language"])
async def define_word(word: str):
    loop = get_running_loop()
    x = await loop.run_in_executor(None, partial(define, word))
    return await send_response(x)