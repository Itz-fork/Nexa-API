# Copyright (c) 2022 Itz-fork

from glob import glob
from os import makedirs
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from os.path import dirname, join, basename, isfile, isdir
from importlib import import_module, invalidate_caches
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from .config.storageConf import path_to


app = FastAPI(docs_url=None, redoc_url=None)


class Start():
    def __init__(self) -> None:
        # Create upload dir if not exists
        if not isdir(path_to):
            makedirs(path_to)
        # Importing routes from "routes" dir
        self.add_routes()
        # Customizing the openapi
        app.openapi = self.nx_openapi


    def add_routes(self):
        routes = glob(join(f"{dirname(__file__)}/routes", "*.py"))
        rr = list(set([basename(f)[:-3] for f in routes if isfile(f) and not f.endswith("__init__.py")]))
        for i in rr:
            try:
                invalidate_caches()
                im = import_module(f"api.routes.{i}")
                app.include_router(im.route)
            except Exception as e:
                print(f"Failed to import route - {i}")
    
    def nx_openapi(self):
        op_sch = get_openapi(
            title="Nexa-APIs 🌊",
            version="0.2.5",
            description="Simple API made for fun 😆!",
            routes=app.routes
        )
        app.openapi_schema = op_sch
        return app.openapi_schema

Start()


# Override default docs and redoc urls
@app.get("/docs", include_in_schema=False)
async def over_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json",
    title="Nexa-APIs 🌊 | Swagger",
    swagger_favicon_url="https://github.com/Itz-fork/Nexa-APIs/raw/master/favicon.ico")

@app.get("/redoc", include_in_schema=False)
async def over_redoc():
    return get_redoc_html(openapi_url="/openapi.json",
    title="Nexa-APIs 🌊 | Redoc",
    redoc_favicon_url="https://github.com/Itz-fork/Nexa-APIs/raw/master/favicon.ico")