# Copyright (c) 2022 - Itz-fork

from httpx import AsyncClient


async def fetch(url, json: bool = True, *args, **kwargs):
    """
    Fetch data from an url
    """
    async with AsyncClient() as hc:
        r = await hc.get(url, *args, **kwargs)
        return r.json() if json else r