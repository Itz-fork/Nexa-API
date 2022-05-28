# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter

from ..functions.reddit import request
from ..functions.response import send_response
from ..models.Search import RedditModel

route = APIRouter()


@route.get(
    "/reddit",
    description="Search for posts in reddit",
    response_model=RedditModel,
    tags=["Search"])
async def reddit_search(q: str, sub: str = None):
    r = await request(q, sub.split(" ") if sub else [])
    return await send_response(r)
