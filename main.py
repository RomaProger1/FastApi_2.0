from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from Public.users import users_router, classes_router
from db import f
import os

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
    port = int(os.environ.get("PORT", 8000))  # Используем порт, указанный в переменной окружения, или 8000 по умолчанию
    uvicorn.run(app, host="0.0.0.0", port=port)  # Запускаем сервер на всех интерфейсах