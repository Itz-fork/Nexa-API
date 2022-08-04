# Copyright (c) 2022 Itz-fork

from aiohttp import ClientSession, ClientResponse
from .errors import ResponseStatusError


class Nexa_API_Tools:
    """
    Access api endpoints with the "Tools" tag
    """

    def __init__(self, api_url: str = None) -> None:
        self.api_url = api_url if api_url else "https://nexa-apis.herokuapp.com/"

    async def _tools_parse_response(self, response: ClientResponse):
        """
        Parse response from the server

        Compatible endpoints:

            - `/password`
            - `/currency`
            - `gen_palette`
        """
        js = await response.json()
        # Checks status
        if not js.get("status") == "ok":
            raise ResponseStatusError(response.status)
        # Parse response
        return js.get("data")

    async def password(self, length: int = 12):
        """
        Generates a random password according to the given length

        ### Arguments

            - `length` :int (optional) = Max length of the generated password. Defaults to `12`
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}password")
            return await self._fun_parse_response(res)

    async def currency(self, origin: str, to: str, amount: float):
        """
        Exchange rate from 'x' to 'y'. Data is scraped from x-rates

        ### Arguments

            - `origin` :str = Origin of the `amount` parameter (Ex: USD, INR, etc)
            - `to` :str = Currency that the `amount` needs to be converted to
            - `amount` :float = Amount
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}currency?origin={origin}&to={to}&amount={amount}")
            return await self._fun_parse_response(res)
