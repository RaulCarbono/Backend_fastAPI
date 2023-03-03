from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Soy el servidor yo mando aqui wey"


@app.get("/url")
async def url():
    return {"url" : "https://pruebas.com/python"}