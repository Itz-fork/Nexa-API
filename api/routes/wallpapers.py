# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from ..functions.reddit import request
from ..functions.response import send_response
from ..config.basic import NX_Basic

route = APIRouter()

@route.get("/wallpaper", description="Fetch wallpapers from subreddits", tags=["Search", "Tools"])
async def walpapers_search(q: str):
    walls = []
    r = await request(q, NX_Basic["subs"])
    try:
        for i in r:
            if i["image"]:
                walls.append(i["image"])
    except:
        pass
    return await send_response(walls)