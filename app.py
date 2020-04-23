import datetime
import os
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

@app.get("/data")
async def data():
    return {
            "time": datetime.datetime.utcnow()
            }


static = StaticFiles(directory="frontend/")

@app.get("/{path:path}", name="catch-all")
async def frontend_catchall(path: str, request: Request):
    # Find static file for path
    path = path.lstrip("/")
    full_path, stat_path = await static.lookup_path(path)

    # If file exists, serve it
    if os.path.isfile(full_path) and stat_path is not None:
        return await static.get_response(path, request.scope)

    # Serve index.html
    return await static.get_response("index.html", request.scope)

