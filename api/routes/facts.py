# Copyright (c) 2022 - Itz-fork

from json import loads
from random import choice
from aiofiles import open
from fastapi import APIRouter

from ..models.Fun import FactsModel
from ..functions.response import send_response


route = APIRouter()


@route.get(
    "/fact",
    description="Get a random fact",
    response_model=FactsModel,
    tags=["Fun"])
async def get_random_fact():
    async with open("api/data/facts.json") as ls:
        fcts = loads(await ls.read())
        return await send_response(choice(list(fcts.values())))