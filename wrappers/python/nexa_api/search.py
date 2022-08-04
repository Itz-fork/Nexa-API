# Copyright (c) 2022 Itz-fork

from aiohttp import ClientSession, ClientResponse
from .errors import ResponseStatusError


class Nexa_API_Search:
    """
    Access api endpoints with the "Search" tag
    """

    def __init__(self, api_url: str = None) -> None:
        self.api_url = api_url if api_url else "https://nexa-apis.herokuapp.com/"

    async def _search_parse_response(self, response: ClientResponse):
        """
        Parse response from the server

        Compatible endpoints:

            - `/ud`
            - `/1337x`
            - `/npm`
            - `/reddit`
            - `/wallpaper`
        """
        js = await response.json()
        # Checks status
        if not js.get("status") == "ok":
            raise ResponseStatusError(response.status)
        # Parse response
        return js.get("data")

    async def ud(self, q: str):
        """
        Search for definitions in urban dictionary

        ### Arguments

            - `q` :str = Word to search
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}ud?q={q}")
            return await self._search_parse_response(res)

    async def s1337x(self, q: str):
        """
        Search for torrents in 1337x

        ### Arguments

            - `q` :str = Query
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}1337x?q={q}")
            return await self._search_parse_response(res)

    async def npm(self, q: str):
        """
        Search for npm packages

        ### Arguments

            - `q` :str = Name of the package
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}npm?q={q}")
            return await self._search_parse_response(res)

    async def reddit(self, q: str, sub: str = None, nsfw: bool = False):
        """
        Search for posts in reddit

        ### Arguments

            - `q` :str = Query
            - `sub` :str = Subreddit to search. By default it search for all the reddit
            - `nsfw` :str (optional) = Whether you want to search for nsfw posts or not. Defaults to `False`
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}reddit?q={q}&sub={sub}&nsfw={nsfw}")
            return await self._search_parse_response(res)

    async def wallpaper(self, q: str, nsfw: bool = False):
        """
        Fetch wallpapers from subreddits

        ### Arguments

            - `q` :str = Query
            - `nsfw` :str (optional) = Whether you want to search for nsfw posts or not. Defaults to `True`
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}wallpaper?q={q}&nsfw={nsfw}")
            return await self._search_parse_response(res)
