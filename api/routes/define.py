# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from PyDictionary import PyDictionary

from ..models.Languages import DefineModel
from ..functions.asyncnx import run_async
from ..functions.response import send_response


route = APIRouter()


def define(word):
    dic = PyDictionary()
    mn = dic.meaning(word[0])
    result = {}
    if type(mn) is dict:
        # Iterate through key value pairs of the dict (not dick)
        for k, v in mn.items():
            result["type"] = k
            result["definition"] = v
    return result

@route.get(
    "/define",
    description="Get the definition of a word",
    response_model=DefineModel,
    tags=["Language"])
async def define_word(word: str):
    x = await run_async(define, word)
    return await send_response(x)