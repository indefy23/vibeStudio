import json
from copy import deepcopy

class PolishAgent:
    """
    Agent responsible for refining the rough timeline.
    It adds animations, keyframes, transitions, and audio polish.
    """
    
    def __init__(self, context=None):
        self.context = context or {}

    def refine_timeline(self, rough_timeline: dict) -> dict:
        """
        Takes a rough timeline and applies polishing rules.
        """
        # Deep copy to avoid modifying original
        refined = deepcopy(rough_timeline)
        
        # 1. Refine Video Track (Transitions)
        refined["video"] = self._polish_video_track(refined.get("video", []))
        
        # 2. Refine Overlays (Animations)
        refined["overlay"] = self._polish_overlays(refined.get("overlay", []))
        
        # 3. Refine Text (Animations)
        refined["text"] = self._polish_text(refined.get("text", []))
        
        # 4. Refine Audio (Fades & Levels)
        refined["audio"] = self._polish_audio(refined.get("audio", []))
        
        return refined

    def _polish_video_track(self, clips):
        """
        Adds transitions between clips where appropriate.
        For PoC, we might just ensure cuts are clean, but let's add metadata.
        """
        polished = []
        for i, clip in enumerate(clips):
            # Default to no transition (cut)
            clip["transition"] = {"type": "cut"}
            
            # Example heuristic: If clip is long (>5s), maybe add a dissolve?
            # For PoC, let's keep it simple: straight cuts are fine.
            # But we could mark the first clip to fade in from black?
            if i == 0:
                clip["effects"] = clip.get("effects", [])
                clip["effects"].append({"type": "fade_in", "duration": 0.5})
            
            polished.append(clip)
        return polished

    def _polish_overlays(self, overlays):
        """
        Adds entrance/exit animations to overlays.
        """
        polished = []
        for overlay in overlays:
            # 1. Ensure position is defined
            if "position" not in overlay:
                overlay["position"] = "center"

            # 2. Ensure scale is reasonable (avoid covering whole screen unless intended)
            if "scale" not in overlay:
                overlay["scale"] = 0.5 # Default to half width

            # 3. Add default animations if none exist
            if "animation" not in overlay:
                # Heuristic: Pop in for memes, Fade in for images
                desc = overlay.get("description", "").lower()
                
                if "meme" in desc or "gif" in desc or "sticker" in desc:
                    overlay["animation"] = {
                        "in": {"type": "pop_in", "duration": 0.3, "easing": "back_out"},
                        "out": {"type": "fade_out", "duration": 0.2}
                    }
                else:
                    overlay["animation"] = {
                        "in": {"type": "fade_in", "duration": 0.5},
                        "out": {"type": "fade_out", "duration": 0.5}
                    }
            
            polished.append(overlay)
        return polished

    def _polish_text(self, text_clips):
        """
        Adds text animations.
        """
        polished = []
        for clip in text_clips:
            if "animation" not in clip:
                # Default text animation
                clip["animation"] = {
                    "in": {"type": "typewriter", "speed": 0.05}, # or slide_up
                    "out": {"type": "fade_out", "duration": 0.2}
                }
            polished.append(clip)
        return polished

    def _polish_audio(self, audio_clips):
        """
        Adds fades to audio clips to prevent clicking.
        """
        polished = []
        for clip in audio_clips:
            # Ensure every audio clip has fade in/out
            if "fades" not in clip:
                clip["fades"] = {
                    "in": 0.1,  # 100ms fade in
                    "out": 0.1  # 100ms fade out
                }
            polished.append(clip)
        return polished
