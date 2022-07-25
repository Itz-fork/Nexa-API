# Copyright (c) 2022 - Itz-fork


from aiofiles import os
from os.path import basename
from fastapi.responses import FileResponse
from fastapi import APIRouter, UploadFile, File

from ..config.storageConf import NX_Strg
from ..functions.response import send_response
from ..functions.storage_helper import write_file, FileSizeIsTooLarge
from ..models.FileServer import UploadModel, DownloadModel, DeleteModel


route = APIRouter()


@route.post(
    "/upload",
    description="Upload a file to the server",
    response_model=UploadModel,
    tags=["File server"])
async def upload_file(file: UploadFile = File(...)):
    try:
        fn = await write_file(file)
        xd = {
            "name": file.filename,
            "id": basename(fn)
        }
        return await send_response(xd)
    except FileSizeIsTooLarge:
        return await send_response("File is too large!", 413)


@route.get(
    "/download/{id}",
    description="Download an uploaded file from the server",
    response_model=DownloadModel,
    tags=["File server"])
async def download_file(id: str):
    fi = NX_Strg["path_to"] + id

    if not await os.path.isfile(fi):
        return await send_response("File not found 🗑️!", 404)

    return FileResponse(fi)


@route.delete(
    "/delete/{id}",
    description="Delete an uploaded file from the server",
    response_model=DeleteModel,
    tags=["File server"])
async def delete_file(id: str):
    fi = NX_Strg["path_to"] + id

    if not await os.path.isfile(fi):
        return await send_response("File not found 🗑️!", 404)

    await os.remove(fi)
    return await send_response(f"File - {id} removed!")
