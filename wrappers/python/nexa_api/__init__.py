# Copyright (c) 2022 Itz-fork

from .fun import Nexa_API_Fun
from .tools import Nexa_API_Tools
from .search import Nexa_API_Search
from .file_server import Nexa_API_FS
from .language import Nexa_API_Language


__version__ = "v0.1"

class Nexa_API(Nexa_API_Fun, Nexa_API_Tools, Nexa_API_Search, Nexa_API_FS, Nexa_API_Language):
    def __init__(self, api_url: str = None) -> None:
        super().__init__(api_url)
