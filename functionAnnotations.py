from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
async def read_item(name: str)->str:
    return f"Hola {name}"