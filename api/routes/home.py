# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from ..functions.response import send_response

route = APIRouter()

@route.get("/")
async def home():
    return await send_response("API is alive 😘!")