# Copyright (c) 2022 - Itz-fork

from os import remove
from colorgram import extract
from fastapi import APIRouter, UploadFile, File

from ..models.Tools import PaletteModel
from ..functions.asyncnx import run_async
from ..functions.response import send_response
from ..functions.storage_helper import write_file, FileSizeIsTooLarge

route = APIRouter()


def gen_colors(data):
    clrs = extract(data[0], data[1])
    final = []
    if data[2] == "hsl":
        for hclr in clrs:
            hpal = [hclr.hsl.h, hclr.hsl.s, hclr.hsl.l]
            final.append(hpal)
    else:
        for rclr in clrs:
            rpal = [rclr.rgb.r, rclr.rgb.g, rclr.rgb.b]
            final.append(rpal)
    return final


@route.post(
    "/gen_palette",
    description="Generate color palettes from images",
    response_model=PaletteModel,
    tags=["Tools"])
async def generate_color_palette(limit: int = 2, type_as: str = "rgb", file: UploadFile = File(...)):
    # Check if the file is an image or not
    if "image" not in file.content_type:
        return await send_response("File is not an image", 406)
    limit = limit if limit <= 6 else 2
    try:
        fn = await write_file(file)
        clrs = await run_async(gen_colors, fn, limit, type_as)
        remove(fn)
        return await send_response(clrs)
    except FileSizeIsTooLarge:
        return await send_response("File is too large!", 413)
