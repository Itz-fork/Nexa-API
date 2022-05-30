# Copyright (c) 2022 - Itz-fork

from sys import getsizeof
from random import sample
from aiofiles import open
from os.path import splitext, isfile
from secrets import token_urlsafe
from ..config.storageConf import NX_Strg


async def gen_name(file):
    while True:
        name = "".join([
            NX_Strg["path_to"],
            "".join(sample(file.filename, 4)),
            token_urlsafe(NX_Strg["length"]),
            splitext(file.filename)[1]])
        if not isfile(name):
            return name


async def write_file(file):
    fn = await gen_name(file)
    async with open(fn, mode="wb") as pp:
        cnt = await file.read()
        # Checks file size
        if getsizeof(cnt) > NX_Strg["limit"]:
            raise FileSizeIsTooLarge("Dammit, too large")
        await pp.write(cnt)
    return fn



# Errors

class FileSizeIsTooLarge(Exception):
    pass