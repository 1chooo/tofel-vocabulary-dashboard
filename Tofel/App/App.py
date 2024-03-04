# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Form, Depends, HTTPException
from Tofel.Utils.Build import build_and_mount_playground

app = FastAPI(
    title="Tofel Vocabulary",
    description="Tofel Vocabulary",
    version="Tofel-v0.0.1-beta",
    docs_url="/docs",
)

os.makedirs("static", exist_ok=True)
app.mount(
    "/static", 
    StaticFiles(directory="static"), 
    name="static",
)

templates = Jinja2Templates(
    directory="templates",
)

# @app.get("/")
# def read_main():
#     return {"message": "This is your main app"}

app = build_and_mount_playground(
    app,
    "/",
    "favicon.ico",
    "/",
)

@app.get('/favicon.ico', include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse(
        './static/favicon.ico',
    )