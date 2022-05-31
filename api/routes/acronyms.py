# Copyright (c) 2022 - Itz-fork

from json import loads
from aiofiles import open
from fastapi import APIRouter

from ..models.Languages import AcronymModel
from ..functions.response import send_response


route = APIRouter()


@route.get(
    "/acronym",
    description="Get the meaning of an internt acronym",
    response_model=AcronymModel,
    tags=["Language"])
async def get_acronym(word: str):
    async with open("api/data/acronyms_list.json") as ls:
        acc = loads(await ls.read())
        return await send_response(acc.get(word.lower()))
