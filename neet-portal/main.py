from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import bot  # Starts the Telegram bot
import os

app = FastAPI()

# Serve static frontend
app.mount("/", StaticFiles(directory="Website", html=True), name="site")

# Serve PDF folders
from pathlib import Path
pdfs_path = Path(__file__).parent / "Website" / "pdfs"
app.mount("/pdfs", StaticFiles(directory=pdfs_path), name="pdfs")
