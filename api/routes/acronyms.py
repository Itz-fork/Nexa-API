# Copyright (c) 2022 Itz-fork

from json import loads
from aiofiles import open
from fastapi import APIRouter
from ..functions.response import send_response


route = APIRouter()


@route.get(
    "/acronym",
    description="Get the meaning of an acronym. In case if you get an empty response, try changing the word into lowercase and try again",
    tags=["Language"])
async def get_acronym(word: str):
    async with open("api/data/acronyms_list.json") as ls:
        acc = loads(await ls.read())
        return await send_response(acc.get(word))
