# Copyright (c) 2022 Itz-fork

from aiohttp import ClientSession, ClientResponse
from .errors import ResponseStatusError


class Nexa_API_Language:
    """
    Access api endpoints with the "Language" tag
    """

    def __init__(self, api_url: str = None) -> None:
        self.api_url = api_url if api_url else "https://nexa-apis.herokuapp.com/"

    async def _lang_parse_response(self, response: ClientResponse):
        """
        Parse response from the server

        Compatible endpoints:

            - `/define`
            - `/acronym`
            - `/tr`
        """
        js = await response.json()
        # Checks status
        if not js.get("status") == "ok":
            raise ResponseStatusError(response.status)
        # Parse response
        return js.get("data")

    async def define(self, word: str):
        """
        Get the definition of an english word along with the type

        ### Arguments

            - `word` :str = Word to search for 
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}define?word={word}")
            return await self._fun_parse_response(res)

    async def acronym(self, word: str):
        """
        Get the meaning of an internt acronym

        ### Arguments

            - `word` :str = Word to search for 
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}acronym?word={word}")
            return await self._fun_parse_response(res)

    async def translate(self, text: str, dest: str = "en"):
        """
        Translate text using google translate

        ### Arguments

            - `text` :str = Text to translate
            - `dest` :str = Code of the destination language
        """
        async with ClientSession() as nxs:
            res = await nxs.get(f"{self.api_url}tr?text={text}&dest={dest}")
            return await self._fun_parse_response(res)
