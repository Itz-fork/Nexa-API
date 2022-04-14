# Copyright (c) 2022 Itz-fork

from httpx import AsyncClient

async def req(url, json=True):
    async with AsyncClient() as hc:
        r = await hc.get(url)
        if json:
            return r.json()
        else:
            return r