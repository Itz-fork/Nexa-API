# Copyright (c) 2022 - Itz-fork

from json import loads
from random import choice
from aiofiles import open
from fastapi import APIRouter

from ..models.Fun import InsultModel
from ..functions.response import send_response


route = APIRouter()


@route.get(
    "/insult",
    description="Insult somebody ( ✧≖ ͜ʖ≖)",
    response_model=InsultModel,
    tags=["Fun"])
async def insult_em():
    async with open("api/data/insults_list.json") as ls:
        fcts = loads(await ls.read())
        return await send_response(choice(list(fcts.values())))