from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI, Response, Path, Query, Body, Header
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse, FileResponse
from Public.users import users_router, classes_router
from db import f

# Загружаем переменные окружения из файла .env
load_dotenv()

app = FastAPI()
f()

app.include_router(users_router)
app.include_router(classes_router())

@app.get('/', response_class=HTMLResponse)
def p_index():
    return "<b> Hello World, FastAPI </b>"

if __name__ == "__main__":
   uvicorn.run(app,host="127.0.0.1", port=8000)