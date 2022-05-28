# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from ..functions.reddit import request
from ..functions.response import send_response

from ..config.basic import NX_Basic
from ..models.Search import WallpaperModel

route = APIRouter()


@route.get(
    "/wallpaper",
    description="Fetch wallpapers from subreddits",
    response_model=WallpaperModel,
    tags=["Search"])
async def walpapers_search(q: str):
    walls = []
    r = await request(q, NX_Basic["subs"])
    for i in r:
        if i["image"]:
            walls.append(i["image"])
        else:
            continue
    return await send_response(walls)
