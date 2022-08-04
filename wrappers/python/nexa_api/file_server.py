# Copyright (c) 2022 Itz-fork

from os import getcwd, path as nxosp
from aiofiles import os, open as nxopen
from aiohttp import ClientSession, ClientResponse
from .errors import ResponseStatusError


class Nexa_API_FS:
    """
    Access api endpoints with the "File Server" tag
    """

    def __init__(self, api_url: str = None, chunk_size=1024 * 6) -> None:
        self.api_url = api_url if api_url else "https://nexa-apis.herokuapp.com/"
        self.download_path = f"{getcwd()}/NxDownloads"
        # Create download path if not exists
        if not os.path.isdir(self.download_path):
            os.makedirs(self.download_path)
        self.chunk_size = chunk_size

    async def _fs_parse_response(self, response: ClientResponse):
        """
        Parse response from the server

        Compatible endpoints:

            - `/upload`
            - `/download`
            - `/delete`
        """
        js = await response.json()
        # Checks status
        if not js.get("status") == "ok":
            raise ResponseStatusError(response.status)
        # Parse response
        return js.get("data")

    async def upload(self, file: str):
        """
        Upload a file to the server

        ### Arguments

            - `file` :str = Path to the file that needs to be uploaded
        """
        async with ClientSession() as nxs:
            with open(file, "rb") as nxfile:
                res = await nxs.post(f"{self.api_url}upload", data={"file": nxfile})
            return await self._fs_parse_response(res)

    async def download(self, id: str):
        """
        Download an uploaded file from the server

        ### Arguments

            - `id` :str = ID of the file that you want to download
        """
        url = f"{self.api_url}download/{id}"
        fname = f"{self.download_path}/{nxosp.basename(url)}"
        async with ClientSession() as nxs:
            async with nxs.get(url, timeout=None) as resp:
                # Checks response status
                if resp.status != 200:
                    ResponseStatusError(resp.status)
                # Checks if the file already has been downloaded
                if os.path.isfile(fname):
                    raise FileExistsError(
                        "The file that you are trying to download is already exists in this system")
                # Write file, chunk by chunk
                async with nxopen(fname, mode="wb") as file:
                    async for chunk in resp.content.iter_chunked(self.chunk_size):
                        await file.write(chunk)
            return await self._fs_parse_response({"status": "ok", "data": {"path": fname}})

    async def delete(self, id: str):
        """
        Delete an uploaded file from the server

        ### Arguments

            - `id` :str = ID of the file that you want to download
        """
        url = f"{self.api_url}delete/{id}"
        async with ClientSession() as nxs:
            resp = await nxs.delete(url)
            return await self._fs_parse_response(resp)
