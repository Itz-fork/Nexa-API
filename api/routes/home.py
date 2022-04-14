# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

route = APIRouter()

@route.get("/", include_in_schema=False)
async def home():
    return RedirectResponse("/docs")