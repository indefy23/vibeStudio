import os
import ffmpeg
import openai
from app.core.config import settings

def get_video_duration(path: str) -> float:
    """Uses ffmpeg.probe to get video duration in seconds."""
    try:
        probe = ffmpeg.probe(path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream:
            return float(video_stream['duration'])
        
        # Fallback to audio if no video
        audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
        if audio_stream:
            return float(audio_stream['duration'])
            
        return 0.0
    except Exception as e:
        print(f"Error probing file {path}: {e}")
        return 0.0

def transcribe_with_openai(path: str, api_key: str = None) -> dict:
    """Uses OpenAI API to transcribe audio."""
    if not api_key:
        api_key = settings.OPENAI_API_KEY
    
    if not api_key:
        print("WARNING: No OPENAI_API_KEY found, returning mock transcription.")
        return {"text": "Mock transcription (Missing Key)", "segments": []}
    
    client = openai.OpenAI(api_key=api_key)
    
    try:
        with open(path, "rb") as audio_file:
            # Note: For long files (>25mb) we would need chunking. 
            # For PoC we assume short files.
            # Using 'verbose_json' to get segments/timestamps
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file, 
                response_format="verbose_json"
            )
            
            # OpenAI Python SDK returns objects, we convert to dict structure similar to local whisper
            return transcript.model_dump() 
            
    except Exception as e:
        print(f"Error transcribing with OpenAI: {e}")
        return {"text": "", "segments": []}

def extract_frame(video_path: str, output_path: str, time: float = 2.0) -> str:
    """
    Extracts a single frame from the video at the specified time.
    Returns the path to the extracted image.
    """
    try:
        (
            ffmpeg
            .input(video_path, ss=time)
            .output(output_path, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return output_path
    except ffmpeg.Error as e:
        print(f"Error extracting frame from {video_path}: {e.stderr.decode('utf8')}")
        return None
