from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fasthtml.common import *
from loguru import logger
from pydantic import BaseModel


class Colors(BaseModel):
    colors: List[str]



app = FastAPI()

@app.get("/")
def read_root(request: Request) -> Colors:
    colors = ["red", "green", "blue"]

    if "application/json" in request.headers.get("accept"):
        return {"colors": colors}

    page = Div(Ol(*[Li(color) for color in colors]))
    return HTMLResponse(to_xml(page))
