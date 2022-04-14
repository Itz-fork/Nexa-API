# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from ..config.wall import subs
from ..functions.reddit import request
from ..functions.response import send_response

route = APIRouter()

@route.get("/wallpaper", description="Fetch wallpapers from subreddits")
async def walpaper(q: str):
    walls = []
    r = await request(q, subs)
    try:
        for i in r:
            if i["image"]:
                walls.append(i["image"])
    except:
        pass
    return await send_response(walls)