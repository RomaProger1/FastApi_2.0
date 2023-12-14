from fastapi import FastAPI, Response, Path, Query, Body, Header
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse, FileResponse
from Public.users import users_router

app = FastAPI()

app.include_router(users_router)


@app.get('/', response_class=HTMLResponse)
def p_index():
    return "<b> Hello World, FastAPI </b>"