# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from ..functions.response import send_response
from ..functions.http_req import fetch
from ..config.basic import NX_Basic

route = APIRouter()


@route.get("/ud", description="Search for definitions in urban dictionary", tags=["Search"])
async def urban_dict_search(q: str):
    ur = (await fetch(NX_Basic["ud_api"].format(q)))["list"]
    results = []
    if ur:
        for r in ur:
            try:
                data = {}
                data["definition"] = r["definition"]
                data["example"] = r["example"]
                data["sounds"] = r["sound_urls"]
                data["author"] = r["author"]
                data["link"] = r["permalink"]
                data["added_on"] = r["written_on"]
                data["likes"] = r["thumbs_up"]
                data["dislikes"] = r["thumbs_down"]
                results.append(data)
            except:
                pass
    return await send_response(results)