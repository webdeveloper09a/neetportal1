from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import bot  # Starts the Telegram bot
import os

app = FastAPI()

# Serve static frontend
app.mount("/", StaticFiles(directory="Website", html=True), name="site")

# Serve PDF folders
app.mount("/pdfs", StaticFiles(directory="pdfs"), name="pdfs")
