# Copyright (c) 2022 Itz-fork

from glob import glob
from fastapi import FastAPI
from os.path import dirname, join, basename, isfile
from importlib import import_module, invalidate_caches
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html


app = FastAPI(docs_url=None, redoc_url=None)

# Override default docs and redoc urls
@app.get("/docs", include_in_schema=False)
async def over_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json",
    title="Nexa-APIs 🌊 | Swagger",
    swagger_favicon_url="/favicon.ico")

@app.get("/redoc", include_in_schema=False)
async def over_redoc():
    return get_redoc_html(openapi_url="/openapi.json",
    title="Nexa-APIs 🌊 | Redoc",
    redoc_favicon_url="/favicon.ico")


# Importing routes from "routes" dir
def add_routes():
    routes = glob(join(f"{dirname(__file__)}/routes", "*.py"))
    rr = list(set([basename(f)[:-3] for f in routes if isfile(f) and not f.endswith("__init__.py")]))
    for i in rr:
        try:
            invalidate_caches()
            im = import_module(f"api.routes.{i}")
            app.include_router(im.route)
        except Exception as e:
            print(e)
            print(f"Failed to import {i}")

add_routes()