import uvicorn
from typing import Optional
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    descricao: str
    valor: float


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# get standard HEADERS
@app.get("/headers")
def read_root(user_agent: Optional[str] = Header(None)):
    return {"user_agent": user_agent}


# get HEADERS entered by user
@app.get("/headers-customized")
def read_root(my_header: Optional[str] = Header(None)):
    return {"my-header": my_header}


# set COOKIE on browser
@app.post("/cookie")
def cookie(response: Response, cookie: Optional[str] = "cookie_standard"):
    response.set_cookie(key="meucookie", value=cookie)
    return {"cookie": True}


# get COOKIE that was set
@app.get("/get-cookie")
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return {"cookie": meucookie}


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
