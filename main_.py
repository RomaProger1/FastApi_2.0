import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def p_index():
    return {"FIO": "Денисов Роман Дмитриевич"}

@app.get("/users", response_class=HTMLResponse)
async def p_users():
    output = "<h3> Phone Number:+7923*****44 </h3>"
    return output

@app.get("/tools", response_class=HTMLResponse)
async def p_tools():
    output = "<h2> <center> C++ Junior <br> UI/UX Designer <br> 3D Artist </center></h2>"
    return output

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=5000)
