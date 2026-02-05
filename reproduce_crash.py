
import ffmpeg
import os

def reproduce():
    # Asset that is actually AUDIO but treated as VIDEO
    audio_as_video = "backend/tests/assets/WhatsApp Ptt 2026-02-01 at 19.23.40.MP3"
    
    if not os.path.exists(audio_as_video):
        print("Asset not found, cannot reproduce exactly.")
        return

    output = "test_crash.mp4"
    
    # Simulating renderer.py logic
    # vid = ffmpeg.input(src).video.trim(...)
    
    try:
        vid = ffmpeg.input(audio_as_video).video.trim(start=0, end=5).setpts('PTS-STARTPTS')
        aud = ffmpeg.input(audio_as_video).audio.filter('atrim', start=0, end=5).filter('asetpts', 'PTS-STARTPTS')
        
        # Concat (trivial 1 clip)
        joined = ffmpeg.concat(vid, aud, v=1, a=1).node
        base_video = joined[0]
        base_audio = joined[1]
        
        out = ffmpeg.output(base_video, base_audio, output)
        print("Running FFmpeg...")
        out.run(overwrite_output=True)
        print("Success?")
    except ffmpeg.Error as e:
        print("Caught FFmpeg Error!")
        print(e.stderr.decode() if e.stderr else "No stderr")
    except Exception as e:
        print(f"Caught Generic Error: {e}")

if __name__ == "__main__":
    reproduce()
