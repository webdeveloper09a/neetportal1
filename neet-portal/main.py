# main.py
import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Website.bot import start_bot
from starlette.responses import FileResponse
import os

app = FastAPI()

# Serve website static files
app.mount("/pdfs", StaticFiles(directory="Website/pdfs"), name="pdfs")
app.mount("/data", StaticFiles(directory="Website/data"), name="data")

@app.get("/")
async def root():
    return FileResponse("Website/index.html")

# Run both API and bot
if __name__ == "__main__":
    import uvicorn
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
