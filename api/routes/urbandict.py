# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from ..functions.response import send_response
from ..functions.http_req import req
from ..config.ud import api_url

route = APIRouter()


@route.get("/ud")
async def urban_dict(q: str):
    ur = (await req(api_url.format(q)))["list"]
    print(ur)
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