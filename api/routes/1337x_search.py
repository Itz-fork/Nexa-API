# Copyright (c) 2022 - Itz-fork

from py1337x import py1337x
from fastapi import APIRouter

from ..models.Search import X1337Model
from ..functions.asyncnx import run_async
from ..functions.response import send_response


route = APIRouter()


def get_1337x(q):
    trnts = py1337x().search(q[0])
    res = {}
    no = 1
    for itm in trnts["items"]:
        res[no] = itm
        no += 1
    return res


@route.get(
    "/1337x",
    description="Search for torrents in 1337x",
    response_model=X1337Model,
    tags=["Search"])
async def search_1337x(q: str):
    resp = await run_async(get_1337x, q)
    return await send_response(resp)
