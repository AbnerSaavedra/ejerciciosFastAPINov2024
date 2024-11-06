from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None
    price: float
    tax: float | None

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    return item


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    q: str | None = None,
    item: Item | None = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results