import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    descricao: str
    valor: float


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, p: bool, q: Optional[str] = None):
    return {"item_id": item_id, "p": p, "q": q}


@app.post("/item")
def add_item(novo_item: Item):
    return novo_item


@app.post("/itens-bulk")
def add_item_bulk(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]


if __name__ == "__main__":
    uvicorn.run(app)
