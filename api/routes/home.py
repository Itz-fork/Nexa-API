# Copyright (c) 2022 - Itz-fork

from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from ..config.apiConf import NX_Conf

route = APIRouter()

@route.get("/", include_in_schema=False)
async def home():
    if NX_Conf["home_redirect"]:
        return RedirectResponse(NX_Conf["redirect_to"])