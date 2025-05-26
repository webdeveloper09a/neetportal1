from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Serve index.html
@app.get("/")
def read_index():
    return FileResponse("Website/index.html")

# Serve static PDF files
app.mount("/pdfs", StaticFiles(directory="Website/pdfs"), name="pdfs")
