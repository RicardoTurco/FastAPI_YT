import uvicorn
from typing import Optional
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    descricao: str
    valor: float


app = FastAPI()


# Message of Wellcome
@app.get("/")
def read_root():
    return {"Hello, I'm a simple example API with FastAPI"}


# get standard HEADERS
# In example, is recupered key "user-agent" ... but, is possible to retrieve any one
@app.get("/headers")
def read_headers(user_agent: Optional[str] = Header(None)):
    return {"user_agent": user_agent}


# get HEADERS entered by user

# OBS:
# Use Postman an example, the "key" must be the same
# in function, with "_"

# Ex:
# "my-header-customized (Postman)
# "my_headercustomized (function)
@app.get("/headers-customized")
def read_headers_customized(my_header_customized: Optional[str] = Header(None)):
    return {"my_header": my_header_customized}


# set COOKIE on browser
@app.post("/cookie")
def cookie(response: Response, cookie: Optional[str] = "cookie_standard"):
    response.set_cookie(key="meucookie", value=cookie)
    return {"cookie": True}


# get COOKIE that was set
@app.get("/get-cookie")
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return {"cookie": meucookie}


# Get parameters in URL (and "query string")
# remember: "q" is OPTIONAL ...

# Ex:
# localhost:8000/items/2/?p=true&q="msg"
@app.get("/items/{item_id}")
def read_item(item_id: int, p: bool, q: Optional[str] = None):
    return {"item_id": item_id, "p": p, "q": q}


# Get a new instance of "Item"
# OBS: The payload of body must be equal of "Item" model
@app.post("/item")
def add_item(novo_item: Item):
    return novo_item


# Get a 2 instances of "Item"
@app.post("/itens-bulk")
def add_item_bulk(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]


if __name__ == "__main__":
    uvicorn.run(app)
