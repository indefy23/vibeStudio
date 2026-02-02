from fastapi import FastAPI
from contextlib import asynccontextmanager
import subprocess

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Check FFmpeg
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ FFmpeg detectado.")
    except FileNotFoundError:
        print("❌ FFmpeg não encontrado no PATH. A renderização não funcionará.")
    yield
    # Shutdown

app = FastAPI(title="vibeStudio Engine", lifespan=lifespan)

from app.api import brain
app.include_router(brain.router, prefix="/api/brain", tags=["brain"])

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "vibe-studio-backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
