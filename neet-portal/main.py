# main.py
import asyncio
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from bot import run_bot  # run_bot() is your async bot runner

app = FastAPI()

# Serve static website from /Website
app.mount("/", StaticFiles(directory="Website", html=True), name="static")

# Serve PDFs
app.mount("/pdfs", StaticFiles(directory="Website/pdfs"), name="pdfs")

# Serve JSON
@app.get("/data/tests.json")
def get_json():
    return FileResponse("Website/data/tests.json", media_type="application/json")

# Run the bot alongside FastAPI
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_bot())
