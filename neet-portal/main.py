from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import bot  # Starts the Telegram bot
import os

app = FastAPI()

# Serve frontend
app.mount("/", StaticFiles(directory="Website", html=True), name="website")

# Serve PDF files
app.mount("/pdfs", StaticFiles(directory="pdfs"), name="pdfs")
