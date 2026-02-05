import json
from statistics import mean

class EvaluationService:
    """
    Evaluates the quality of the generated timeline based on structural metrics.
    """
    
    def evaluate_project(self, context: dict, timeline: dict) -> dict:
        """
        Generates an evaluation report with score and feedback.
        """
        video_tracks = timeline.get("video", [])
        overlay_tracks = timeline.get("overlay", [])
        audio_tracks = timeline.get("audio", [])
        text_tracks = timeline.get("text", [])
        
        metrics = self._calculate_metrics(video_tracks, overlay_tracks, audio_tracks)
        score = self._calculate_score(metrics)
        feedback = self._generate_feedback(metrics)
        
        return {
            "score": score,
            "metrics": metrics,
            "feedback": feedback,
            "suggestions": self._generate_suggestions(metrics)
        }

    def _calculate_metrics(self, video, overlay, audio):
        """
        Calculates objective metrics from timeline data.
        """
        # 1. Pacing Analysis (Shot Duration)
        durations = []
        total_duration = 0
        for clip in video:
            start = clip.get("start", 0)
            end = clip.get("end", 5) # Default assumption
            dur = end - start
            durations.append(dur)
            total_duration += dur
            
        avg_shot_duration = mean(durations) if durations else 0
        shot_count = len(durations)
        
        # 2. Overlay Density
        # Simple heuristic: count overlays per minute
        minutes = total_duration / 60 if total_duration > 0 else 1
        overlays_per_minute = len(overlay) / minutes
        
        # 3. Audio Layering
        # Check if we have background music + sfx
        has_music = any("music" in c.get("description", "").lower() for c in audio)
        has_sfx = any("sfx" in c.get("description", "").lower() for c in audio)
        
        return {
            "total_duration": total_duration,
            "avg_shot_duration": avg_shot_duration,
            "shot_count": shot_count,
            "overlays_per_minute": overlays_per_minute,
            "has_music": has_music,
            "has_sfx": has_sfx,
            "overlay_count": len(overlay),
            "text_count": len(overlay)
        }

    def _calculate_score(self, metrics):
        """
        Calculates a 0-100 score based on metrics.
        """
        score = 70 # Base score
        
        # Pacing bonus (Dynamic is good for this project context)
        if 2.0 <= metrics["avg_shot_duration"] <= 5.0:
            score += 10
        elif metrics["avg_shot_duration"] > 10.0:
            score -= 10
            
        # Overlay bonus (Visual interest)
        if metrics["overlays_per_minute"] > 5:
            score += 10
        elif metrics["overlays_per_minute"] < 1:
            score -= 5
            
        # Audio polish
        if metrics["has_music"]: score += 5
        if metrics["has_sfx"]: score += 5
        
        return min(100, max(0, score))

    def _generate_feedback(self, metrics):
        feedback = []
        
        if metrics["avg_shot_duration"] > 8.0:
            feedback.append("Pacing feels slow. Consider more cuts or b-roll.")
        elif metrics["avg_shot_duration"] < 1.5:
            feedback.append("Pacing is very fast. Ensure information is readable.")
        else:
            feedback.append("Good pacing balance.")
            
        if metrics["overlays_per_minute"] < 2:
            feedback.append("Visuals might be static. Add more overlays/GIFs.")
            
        if not metrics["has_music"]:
            feedback.append("Missing background music reduces engagement.")
            
        return feedback

    def _generate_suggestions(self, metrics):
        suggestions = []
        if metrics["overlay_count"] == 0:
            suggestions.append("Try adding reaction GIFs to emphasize key moments.")
        if metrics["text_count"] == 0:
            suggestions.append("Add subtitles or keyword overlays for retention.")
        return suggestions
