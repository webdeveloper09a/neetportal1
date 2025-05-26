from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="Website/static"), name="static")
app.mount("/pdfs", StaticFiles(directory="Website/pdfs"), name="pdfs")
templates = Jinja2Templates(directory="Website/templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    with open("Website/data/tests.json", "r") as f:
        tests_data = json.load(f)
    return templates.TemplateResponse("index.html", {"request": request, "tests": tests_data})
