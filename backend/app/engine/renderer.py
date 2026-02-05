import ffmpeg
import json
import os
import random
from typing import List

class Renderer:
    def render_timeline(self, timeline_json_path: str, output_path: str, assets_path: str, asset_map: dict = None):
        with open(timeline_json_path, 'r') as f:
            data = json.load(f)
        
        # Handle schema structure (fallback to legacy if needed)
        # New structure has "video", "audio", "overlay". Old has "clips" or "timeline".
        video_clips = data.get("video", [])
        if not video_clips:
            video_clips = data.get("timeline", data.get("clips", []))
            
        overlay_clips = data.get("overlay", [])
        audio_clips = data.get("audio", [])       

        if not video_clips:
             raise ValueError("No video clips found")

        # 1. Build Base Video (Cuts)
        concat_inputs = []
        input_idx = 0
        
        # Helper to resolve path
        def get_path(aid):
            aid_str = str(aid).strip()
            print(f"  [DEBUG] Resolving asset: '{aid_str}'")
            if asset_map:
                if aid_str in asset_map:
                    p = asset_map[aid_str]
                    print(f"  [DEBUG] Found in map: {p}")
                    # Convert to absolute path if relative
                    if not os.path.isabs(p):
                         # If it starts with ./, it's relative to project root (CWD)
                         # Otherwise it might be relative to assets_path, but manifest uses project root
                         p = os.path.abspath(p)
                    
                    if os.path.exists(p):
                        print(f"  [DEBUG] Final absolute path exists: {p}")
                        return p
                    else:
                        print(f"  [ERROR] Asset path from map does NOT exist: {p}")
            
            # Fallback to assets_path (usually project_dir/assets)
            p = os.path.join(assets_path, aid_str)
            if not os.path.exists(p):
                 # Try with original filename if it's a UUID that might not be in assets_path
                 print(f"  [DEBUG] Fallback path does NOT exist: {p}")
            else:
                 print(f"  [DEBUG] Fallback path exists: {p}")
            return p

        # Base Video Streams
        for clip in video_clips:
            input_idx += 1
            # Special Handling for Placeholder (Integrity Filter)
            if clip["asset_id"] == "color_placeholder":
                start, end = clip.get("start", 0), clip.get("end", 5.0)
                duration = end - start
                # Dark Gray Background (Visual Noise Placeholder)
                # Use jitter to avoid cache collisions
                d_jit = duration + random.uniform(0.0001, 0.0009)
                vid = ffmpeg.input(f'color=c=0x1a1a1a:s=1280x720:d={d_jit}', f='lavfi').trim(duration=duration).setpts('PTS-STARTPTS')
                
                d_jit_aud = duration + random.uniform(0.0001, 0.0009)
                # Use asetpts for audio
                aud = ffmpeg.input(f'anullsrc=r=44100:cl=stereo:d={d_jit_aud}', f='lavfi').audio.filter('atrim', duration=duration).filter('asetpts', 'PTS-STARTPTS')
                concat_inputs.extend([vid, aud])
                continue

            src = get_path(clip["asset_id"])
            start, end = clip.get("start", 0), clip.get("end", None)
            
            # Check if asset is Audio-only (e.g. MP3 in video track)
            # This happens if the Agent selects an audio file as the main content base.
            is_audio_only = src.lower().endswith(('.mp3', '.wav', '.m4a', '.flac', '.aac'))
            
            # Check if asset is static image (WebP, PNG, JPG)
            # This happens if the Agent selects an image as video content
            is_static_image = src.lower().endswith(('.webp', '.png', '.jpg', '.jpeg'))
            
            if is_audio_only:
                # Create dummy colored video (Dark Gray) instead of black
                duration = end - start if end and start is not None else 5.0 # Fallback
                d_jit = duration + random.uniform(0.0001, 0.0009)
                vid = ffmpeg.input(f'color=c=0x1a1a1a:s=1280x720:d={d_jit}', f='lavfi').trim(duration=duration).setpts('PTS-STARTPTS')
                # Audio comes from the asset
                aud = ffmpeg.input(src, probesize=5000000+input_idx).audio.filter('atrim', start=start, end=end).filter('asetpts', 'PTS-STARTPTS')
            elif is_static_image:
                # Create video from static image with loop
                duration = end - start if end and start is not None else 5.0 # Fallback
                
                if src.lower().endswith('.webp'):
                    # WebP: loop option often fails with libwebp demuxer. Use filter loop instead.
                    # Loop frame 0 indefinitely, then trim.
                    vid = ffmpeg.input(src, probesize=5000000+input_idx).filter('loop', loop=-1, size=1, start=0).filter('scale', 1280, 720).filter('trim', duration=duration).setpts('PTS-STARTPTS')
                else:
                    # PNG/JPG: input loop works fine
                    vid = ffmpeg.input(src, loop=1, t=duration, probesize=5000000+input_idx).filter('scale', 1280, 720).setpts('PTS-STARTPTS')
                
                # No audio for static images
                d_jit_aud = duration + random.uniform(0.0001, 0.0009)
                aud = ffmpeg.input(f'anullsrc=r=44100:cl=stereo:d={d_jit_aud}', f='lavfi').audio.filter('atrim', duration=duration).filter('asetpts', 'PTS-STARTPTS')
            else:
                # Normal video file
                # Use same input node for both streams to avoid divergence
                inp = ffmpeg.input(src, probesize=5000000+input_idx)
                vid = inp.video.trim(start=start, end=end).setpts('PTS-STARTPTS')
                aud = inp.audio.filter('atrim', start=start, end=end).filter('asetpts', 'PTS-STARTPTS')
                
            concat_inputs.extend([vid, aud])

        # Create the Base Stream (Concatenated)
        joined = ffmpeg.concat(*concat_inputs, v=1, a=1).node
        base_video = joined[0]
        base_audio = joined[1]

        # 2. visual Overlays (GIFs/Images)
        # We assume overlays are relative to the FINAL timeline time 0.0
        # Since 'concat' resets PTS, the output of base_video starts at 0.0.
        
        current_video_stream = base_video
        
        for overlay in overlay_clips:
            input_idx += 1
            src = get_path(overlay["asset_id"])
            start_at = overlay.get("start_at", 0)
            duration = overlay.get("duration", 2.0)
            
            # Skip invalid overlays
            if duration <= 0:
                print(f"  [WARN] Skipping overlay {overlay['asset_id']} with invalid duration: {duration}")
                continue
            
            # Input overlay asset
            input_kwargs = {}
            # GIF: use stream_loop=-1 for infinite loop
            if src.lower().endswith('.gif'):
                input_kwargs['stream_loop'] = -1
            # Static Images (PNG/JPG): use loop=1
            elif src.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_kwargs['loop'] = 1
            # WebP: NO loop parameter (causes "Option not found" error in FFmpeg 7.1)
            # We rely on trim+setpts to control duration
                
            ov_input = ffmpeg.input(src, probesize=5000000+input_idx, **input_kwargs)
            
            # --- SCALE LOGIC ---
            # Default scale is 300px wide (fixed width) or factor of main video
            # Schema: scale (float, e.g. 0.5 mean 50% width) or default fixed 350
            scale_factor = overlay.get("scale", None)
            
            if scale_factor and isinstance(scale_factor, (float, int)):
                 # Scale relative to main video width (w * factor)
                 # Since we don't know main w at filter time easily without probe, we use expression `iw*scale`?
                 # No, better to use fixed width expression `W*scale` where W is main video width.
                 # filter('scale', w='iw*0.5', h=-1) refers to input width.
                 # To refer to main video W, we do it in overlay filter? No, scale filter runs on input.
                 # For simplicity, we stick to fixed width or simple heuristic.
                 # Let's support: < 1.0 = relative, > 1.0 = pixels
                 if scale_factor <= 2.0:
                     # Relative to standard 1280 width
                     width = int(1280 * scale_factor)
                 else:
                     width = int(scale_factor)
            else:
                width = 350 # Default width
            
            # Scale overlay and TRIM to duration (0-based)
            # Removed redundant setpts=PTS-STARTPTS as input usually starts at 0 and trim keeps it relative if start=0
            ov_scaled = ov_input.video.filter('scale', width, -1).filter('trim', duration=duration)
            
            # --- ANIMATION LOGIC (Refinement) ---
            anim = overlay.get("animation", {})
            
            # 1. Fade In / Pop In (Simulated as fast fade)
            in_anim = anim.get("in", {})
            if in_anim and in_anim.get("type") in ["fade_in", "pop_in"]:
                fade_dur = in_anim.get("duration", 0.5)
                # Ensure fade duration isn't longer than the clip itself
                fade_dur = min(fade_dur, duration)
                # alpha=1 forces fade on alpha channel too for transparency
                ov_scaled = ov_scaled.filter('fade', type='in', start_time=0, duration=fade_dur, alpha=1)

            # 2. Fade Out
            out_anim = anim.get("out", {})
            if out_anim and out_anim.get("type") == "fade_out":
                fade_dur = out_anim.get("duration", 0.5)
                fade_dur = min(fade_dur, duration)
                start_fade = max(0, duration - fade_dur)
                ov_scaled = ov_scaled.filter('fade', type='out', start_time=start_fade, duration=fade_dur, alpha=1)
            
            # 3. Time Shift (PTS)
            # CRITICAL: Shift PTS to start_at so overlay appears at correct time without relying on 'enable'
            # TB is the timebase unit
            ov_scaled = ov_scaled.filter('setpts', f'PTS-STARTPTS+({start_at}/TB)')

            # --- POSITION LOGIC ---
            # Schema: position (string) -> center, top_left, top_right, bottom_left, bottom_right
            pos = overlay.get("position", "center")
            padding = 20
            
            if pos == "center":
                x_expr = "(W-w)/2"
                y_expr = "(H-h)/2"
            elif pos == "top_left":
                x_expr = f"{padding}"
                y_expr = f"{padding}"
            elif pos == "top_right":
                x_expr = f"W-w-{padding}"
                y_expr = f"{padding}"
            elif pos == "bottom_left":
                x_expr = f"{padding}"
                y_expr = f"H-h-{padding}"
            elif pos == "bottom_right":
                x_expr = f"W-w-{padding}"
                y_expr = f"H-h-{padding}"
            else:
                x_expr = "(W-w)/2"
                y_expr = "(H-h)/2"

            # Apply overlay
            # eof_action='pass' ensures main video continues after overlay ends
            current_video_stream = current_video_stream.overlay(
                ov_scaled, 
                x=x_expr, 
                y=y_expr, 
                eof_action='pass'
            )
            
        # 2.5 Text Overlays (Subtitles fallback)
        text_clips = data.get("text", [])
        if text_clips:
            try:
                # Create srt file in output dir
                out_dir = os.path.dirname(output_path)
                srt_path = os.path.join(out_dir, "overlays.srt")
                
                self._generate_srt(text_clips, srt_path)
                
                # Apply subtitles filter
                # Alignment=5 (Middle Center), Fontname=Arial, FontSize=24 (relative to video height implies specific sizing logic but ASS uses points)
                # PrimaryColour=&H00FFFFFF (White), OutlineColour=&H00000000 (Black), BorderStyle=1, Outline=2
                # Use relative path to avoid escaping issues with Drive Letter Colon
                # FFmpeg filters hate colons in absolute paths (e.g. C:/)
                try:
                    srt_path_rel = os.path.relpath(srt_path).replace('\\', '/')
                    srt_path_filter = srt_path_rel
                    print(f"  [INFO] Using relative path for subtitles: {srt_path_filter}")
                except Exception as e:
                    # Fallback for cross-drive paths
                    print(f"  [WARN] Could not get relative path: {e}")
                    srt_path_filter = srt_path.replace('\\', '/').replace(':', '\\\\:')
                
                style = "Alignment=10,Fontname=Arial,FontSize=28,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2"
                current_video_stream = current_video_stream.filter('subtitles', srt_path_filter, force_style=style)
                print(f"  [INFO] Applied subtitles from {srt_path}")
            except Exception as e:
                print(f"  [WARN] Failed to apply subtitles: {e}")

        # 3. Audio Mixing (SFX)
        # We use amix. First input is base_audio.
        # Secondary inputs must be delayed using 'adelay' to start at 'start_at'.
        
        audio_inputs = [base_audio]
        
        for sfx in audio_clips:
            input_idx += 1
            src = get_path(sfx["asset_id"])
            
            # CRITICAL: Check if file has audio stream to avoid ":a matches no streams" error
            duration_sec = 0
            try:
                probe = ffmpeg.probe(src)
                has_audio = any(stream['codec_type'] == 'audio' for stream in probe['streams'])
                duration_sec = float(probe['format']['duration'])
                if not has_audio:
                    print(f"  [WARN] Skipping audio track for {src} (No audio stream found)")
                    continue
            except:
                print(f"  [WARN] Could not probe {src}, skipping audio.")
                continue

            start_at = sfx.get("start_at", 0)
            
            # Input sfx
            sfx_stream = ffmpeg.input(src, probesize=5000000+input_idx).audio
            
            # --- AUDIO FADES ---
            fades = sfx.get("fades", {})
            if fades:
                if "in" in fades:
                    fade_in_dur = float(fades["in"])
                    if fade_in_dur > 0:
                        sfx_stream = sfx_stream.filter('afade', type='in', start_time=0, duration=fade_in_dur)
                
                if "out" in fades and duration_sec > 0:
                    fade_out_dur = float(fades["out"])
                    if fade_out_dur > 0:
                        start_fade = max(0, duration_sec - fade_out_dur)
                        sfx_stream = sfx_stream.filter('afade', type='out', start_time=start_fade, duration=fade_out_dur)

            # Delay (adelay expects milliseconds)
            delay_ms = int(start_at * 1000)
            # adelay=Ms|Ms (stereo)
            sfx_delayed = sfx_stream.filter('adelay', f"{delay_ms}|{delay_ms}")
            
            # Adjust volume? volume=0.8
            if "vol" in sfx:
                 sfx_delayed = sfx_delayed.filter('volume', sfx["vol"])
                 
            audio_inputs.append(sfx_delayed)

        # Mix all audios
        if len(audio_inputs) > 1:
            # duration=first (base video length determines total length)
            mixed_audio = ffmpeg.filter(audio_inputs, 'amix', inputs=len(audio_inputs), duration='first')
        else:
            mixed_audio = base_audio

        # 4. Output
        out = ffmpeg.output(current_video_stream, mixed_audio, output_path)
            
        try:
            out.run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        except ffmpeg.Error as e:
            # Safe decode
            stdout = e.stdout.decode('utf8') if e.stdout else "None"
            stderr = e.stderr.decode('utf8') if e.stderr else "None"
            print('ffmpeg stdout:', stdout)
            print('ffmpeg stderr:', stderr)
            raise e
        
        return output_path

    def _generate_srt(self, text_clips, output_path):
        import datetime
        
        def format_time(seconds):
            td = datetime.timedelta(seconds=seconds)
            total_seconds = int(td.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            secs = total_seconds % 60
            millis = int(td.microseconds / 1000)
            return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

        with open(output_path, 'w', encoding='utf-8') as f:
            for i, clip in enumerate(text_clips, 1):
                start = clip.get("start_at", 0)
                # Ensure start is float
                start = float(start)
                duration = clip.get("duration", 2.0)
                end = start + float(duration)
                content = clip.get("content", "")
                
                f.write(f"{i}\n")
                f.write(f"{format_time(start)} --> {format_time(end)}\n")
                f.write(f"{content}\n\n")

