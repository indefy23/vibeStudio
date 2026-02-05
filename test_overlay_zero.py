import ffmpeg

# Simular o problema: overlay com duration=0
try:
    base = ffmpeg.input('color=c=black:s=1280x720:d=5', f='lavfi')
    overlay_src = "backend/tests/assets/boston-dynamics-robot-dog.gif"
    
    # Problema: duration=0
    ov = ffmpeg.input(overlay_src, ignore_loop=0).video.filter('scale', 300, -1).filter('trim', duration=0).filter('setpts', 'PTS-STARTPTS')
    
    result = base.overlay(ov, x='(W-w)/2', y='(H-h)/2', enable='between(t,2,2)')
    
    out = ffmpeg.output(result, 'test_overlay_zero.mp4')
    out.run(overwrite_output=True)
    print("Success?")
except ffmpeg.Error as e:
    print("FFmpeg Error!")
    print(e.stderr.decode() if e.stderr else "No stderr")
