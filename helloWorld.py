from fastapi import FastAPI

app = FastAPI()

@app.get('/holaMundo')
def home():
    return {"message": "Hello world"}