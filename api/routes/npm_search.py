# Copyright (c) 2022 Itz-fork

from fastapi import APIRouter
from ..config.basic import NX_Basic
from ..functions.http_req import fetch
from ..functions.response import send_response

route = APIRouter()


@route.get("/npm", description="Search for npm packages", tags=["Search"])
async def npm_search(q: str):
    resp = await fetch(NX_Basic["npm_api"].format(q))
    packages = []
    for pac in resp["objects"]:
        pp = {}
        pack = pac["package"]
        pp["name"] = pack["name"]
        pp["version"] = pack["version"]
        pp["author"] = pack["author"]["name"] if "author" in pack else ""
        pp["date"] = pack["date"]
        pp["about"] = pack["description"] if "description" in pack else ""
        pp["links"] = pack["links"] if "links" in pack else ""
        pp["keywords"] = pack["keywords"] if "keywords" in pack else ""
        pp["publisher"] = pack["publisher"]
        pp["maintainers"] = pack["maintainers"]
        packages.append(pp)
    return await send_response(packages)