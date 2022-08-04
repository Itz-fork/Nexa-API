# Copyright (c) 2022 Itz-fork

from aiohttp import ClientSession, ClientResponse
from .errors import ResponseStatusError


class Nexa_API_Fun:
    """
    Access api endpoints with the "Fun" tag
    """

    def __init__(self, api_url: str = None) -> None:
        self.api_url = api_url if api_url else "https://nexa-apis.herokuapp.com/"

    async def _fun_parse_response(self, response: ClientResponse):
        """
        Parse response from the server

        Compatible endpoints:

            - `/fact`
            - `/insult`
        """
        js = await response.json()
        # Checks status
        if not js.get("status") == "ok":
            raise ResponseStatusError(response.status)
        # Parse response
        return js.get("data")

    async def fact(self):
        """
        Get a random fact

        ### Arguments

            `None`
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}fact")
            return await self._fun_parse_response(res)

    async def insult(self):
        """
        Get a insult/comeback to insult someone

        ### Arguments

            `None`
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}insult")
            return await self._fun_parse_response(res)
