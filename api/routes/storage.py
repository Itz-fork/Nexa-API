# Copyright (c) 2022 Itz-fork

from sys import getsizeof
from random import sample
from os.path import splitext, basename
from aiofiles import open, os
from secrets import token_urlsafe
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from ..functions.response import send_response
from ..config.storageConf import NX_Strg


route = APIRouter()


@route.post("/upload", description="Upload a file to the server", tags=["File server"])
async def upload_file(file: UploadFile = File(...)):
    async def gen_name():
        while True:
            name = "".join([
                NX_Strg["path_to"],
                "".join(sample(file.filename, 4)),
                token_urlsafe(NX_Strg["length"]),
                splitext(file.filename)[1]])
            if not await os.path.isfile(name):
                return name

    fn = await gen_name()
    async with open(fn, mode="wb") as pp:
        cnt = await file.read()
        # Checks file size
        if getsizeof(cnt) > NX_Strg["limit"]:
            return await send_response("File is too large!", 413)
        await pp.write(cnt)
    xd = {
        "name": file.filename,
        "id": basename(fn)
    }
    return await send_response(xd)


@route.get("/download/{id}", description="Download an uploaded file from the server", tags=["File server"])
async def download_file(id: str):
    fi = NX_Strg["path_to"] + id

    if not await os.path.isfile(fi):
        return await send_response("File not found 🗑️!", 404)

    return FileResponse(fi)


@route.delete("/delete/{id}", description="Delete an uploaded file from the server", tags=["File server"])
async def delete_file(id: str):
    fi = NX_Strg["path_to"] + id

    if not await os.path.isfile(fi):
        return await send_response("File not found 🗑️!", 404)

    await os.remove(fi)
    return await send_response(f"File - {id} removed!")
