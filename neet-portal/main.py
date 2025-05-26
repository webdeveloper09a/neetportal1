from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
import json

app = FastAPI()

# Serve frontend
@app.get("/")
def serve_index():
    return FileResponse("Website/index.html")

# Serve static files
app.mount("/Website", StaticFiles(directory="Website"), name="Website")

# Serve PDFs
pdfs_path = Path(__file__).parent / "Website" / "pdfs"
app.mount("/pdfs", StaticFiles(directory=pdfs_path), name="pdfs")

# Serve test data
@app.get("/data/tests.json")
def get_tests():
    return FileResponse("Website/data/tests.json")
