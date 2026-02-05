from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from app.models.edition import Edition, Asset
from app.engine.ffmpeg_wrapper import FFmpegEngine
import shutil
import os
import uuid
import asyncio

router = APIRouter()

ASSETS_DIR = "assets"
OUTPUT_DIR = "exports"

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@router.post("/assets/upload")
async def upload_asset(file: UploadFile = File(...)):
    """
    Recebe um arquivo de vídeo/imagem e salva localmente.
    Retorna o Asset ID e Path para ser usado no Edition JSON.
    """
    # Generate unique ID
    asset_id = str(uuid.uuid4())[:8]
    extension = os.path.splitext(file.filename)[1]
    filename = f"{asset_id}{extension}"
    file_path = os.path.join(ASSETS_DIR, filename)
    
    # Save file
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")
        
    # Return Asset Object partial
    # In a real app we would probe duration with ffprobe here
    return {
        "id": asset_id,
        "src": os.path.abspath(file_path), # Use Absolute Path for FFmpeg
        "type": "video" 
    }

@router.post("/render")
async def render_edition(edition: Edition):
    """
    Executa o FFmpeg baseado no Edition JSON e retorna o vídeo renderizado.
    Note: Em produção, isso seria async (job queue e websocket).
    Aqui usamos wait direto para simplificar a prova de conceito.
    """
    engine = FFmpegEngine()
    
    output_filename = f"render_{uuid.uuid4().hex[:8]}.mp4"
    output_path = os.path.abspath(os.path.join(OUTPUT_DIR, output_filename))
    
    try:
        print(f"Starting render for {output_path}")
        # Run FFmpeg (Await execution)
        final_path = await engine.render_async(edition, output_path)
        
        # Verify file exists
        if not os.path.exists(final_path):
             raise Exception("File not created by FFmpeg")
             
        return FileResponse(final_path, media_type="video/mp4", filename="output.mp4")

    except Exception as e:
        print(f"Render Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
