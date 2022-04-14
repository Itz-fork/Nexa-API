# Copyright (c) 2022 Itz-fork

from glob import glob
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from os.path import dirname, join, basename, isfile
from importlib import import_module, invalidate_caches
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html


app = FastAPI(docs_url=None, redoc_url=None)

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
            print(f"Failed to import route - {i}")

add_routes()


# Modifying openapi
def nx_openapi():
    op_sch = get_openapi(
        title="Nexa-APIs 🌊",
        version="0.2.4",
        description="Simple API made for fun 😆!",
        routes=app.routes
    )
    app.openapi_schema = op_sch
    return app.openapi_schema

app.openapi = nx_openapi