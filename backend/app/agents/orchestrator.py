import os
import json
from app.core.config import settings
from app.services.analysis_service import AnalysisService
from app.agents.crew import EditorCrew
from app.agents.polish_agent import PolishAgent
from app.services.evaluation_service import EvaluationService
from app.engine.renderer import Renderer
from app.schemas.manifest import ProjectManifest, ProjectStatus

class Orchestrator:
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.project_dir = os.path.join(settings.STORAGE_PATH, project_id)
        self.manifest_path = os.path.join(self.project_dir, "manifest.json")
        self.renderer = Renderer()
        
        # Load Manifest
        with open(self.manifest_path, 'r') as f:
            data = json.load(f)
            self.manifest_data = data
            # Helper object, not strictly synced back until we write
            self.manifest_obj = ProjectManifest(**data)

    def run(self):
        """Orchestrates the build pipeline."""
        try:
            # 1. ANALYSIS Phase
            self._update_status("running", "analysis")
            analyzer = AnalysisService(self.project_dir, self.manifest_obj)
            context = analyzer.analyze_project()
            
            # Save Context
            with open(os.path.join(self.project_dir, "context.json"), "w") as f:
                json.dump(context, f, indent=2)

            # 2. EDITING Phase (Agent)
            self._update_status("running", "editing")
            crew = EditorCrew(context)
            result = crew.run()
            
            # CrewAI returns a string (often), we need to ensure it's valid JSON
            # Ideally the Agent output is strictly JSON constraint.
            # We'll try to parse it.
            try:
                # If result is an object with .raw or similar from CrewAI < 0.28
                if hasattr(result, 'raw'):
                    raw_result = result.raw
                else:
                    raw_result = str(result)
                
                # Cleanup potential markdown code blocks
                if "```json" in raw_result:
                    raw_result = raw_result.split("```json")[1].split("```")[0]
                elif "```" in raw_result:
                    raw_result = raw_result.split("```")[1].split("```")[0]
                    
                timeline_data = json.loads(raw_result)
            except Exception as e:
                print(f"Error parsing Agent output: {result}")
                # Fallback purely for PoC continuity if Agent fails to output valid JSON
                timeline_data = {"clips": []}

            # Integrity Check & Initial Sanitization
            self._sanitize_timeline(timeline_data, context)

            # 2.5 REFINEMENT Phase (Polish Agent)
            # O PolishAgent agora é responsável por garantir que as regras de estilo e animação
            # sejam aplicadas de forma coerente após a estruturação bruta.
            self._update_status("running", "refinement")
            print("[Orchestrator] Running PolishAgent for coherence and style...")
            polisher = PolishAgent(context)
            refined_timeline = polisher.refine_timeline(timeline_data)
            
            # Save Timelines for audit
            rough_path = os.path.join(self.project_dir, "timeline_rough.json")
            with open(rough_path, "w") as f:
                json.dump(timeline_data, f, indent=2)

            refined_path = os.path.join(self.project_dir, "timeline_refined.json")
            with open(refined_path, "w") as f:
                json.dump(refined_timeline, f, indent=2)

            # 2.6 EVALUATION Phase
            self._update_status("running", "evaluation")
            print("[Orchestrator] Running EvaluationService...")
            evaluator = EvaluationService()
            evaluation_report = evaluator.evaluate_project(context, refined_timeline)
            
            eval_path = os.path.join(self.project_dir, "evaluation.json")
            with open(eval_path, "w") as f:
                json.dump(evaluation_report, f, indent=2)

            # Update Manifest Stages
            if "stages" not in self.manifest_data:
                self.manifest_data["stages"] = {}
            self.manifest_data["stages"]["composition"] = "timeline_rough.json"
            self.manifest_data["stages"]["refinement"] = "timeline_refined.json"
            self.manifest_data["stages"]["evaluation"] = "evaluation.json"
            
            # Persist manifest updates immediately before rendering
            with open(self.manifest_path, "w") as f:
                json.dump(self.manifest_data, f, indent=2)

            # 3. RENDERING Phase (Deterministic)
            self._update_status("running", "rendering")
            output_videopath = os.path.join(self.project_dir, "final_video.mp4")
            assets_path = os.path.join(self.project_dir, "assets")
            
            # Create Path Map
            asset_map = {}
            for asset in self.manifest_obj.assets:
                asset_map[asset.id] = asset.path
            
            self.renderer.render_timeline(
                refined_path, # Use REFINED timeline now
                output_videopath,
                assets_path,
                asset_map=asset_map
            )
            
            # 4. FINISH
            self._update_status("completed", "completed")
            
        except Exception as e:
            print(f"Orchestrator failed: {e}")
            import traceback
            traceback.print_exc()
            self._update_status("error", "error")
            raise e

    def _update_status(self, status, stage):
        self.manifest_data["status"] = status
        self.manifest_data["current_stage"] = stage
        with open(self.manifest_path, "w") as f:
            json.dump(self.manifest_data, f, indent=2)

    def _sanitize_timeline(self, timeline_data, context):
        """
        Enforce Hard Rules:
        1. No AUDIO assets in VIDEO track.
           - Move to Audio track.
           - Replace with PLACEHOLDER in Video track (to keep duration/sync).
        """
        assets_map = {a['id']: a for a in context.get('assets_analysis', [])}
        video_track = timeline_data.get('video', [])
        audio_track = timeline_data.get('audio', [])
        
        # We need to track timeline time to correctly place moved audio
        current_time = 0.0
        
        for i, clip in enumerate(video_track):
            asset_id = clip.get('asset_id')
            asset = assets_map.get(asset_id)
            
            # Calculate clip duration
            start = clip.get('start', 0.0)
            end = clip.get('end')
            if end is not None:
                duration = end - start
            else:
                # Fallback if no end (rare)
                duration = 5.0 
            
            if asset and asset.get('type') == 'audio':
                print(f"[Sanitizer] Violation: Audio {asset_id} in Video Track. Fixing...")
                
                # 1. Move to Audio Track
                audio_entry = {
                    "asset_id": asset_id,
                    "start_at": current_time,
                    "vol": 1.0,
                    "description": "Moved from Video Track"
                }
                audio_track.append(audio_entry)
                
                # 2. Replace in Video Track with Placeholder
                clip['asset_id'] = "color_placeholder"
                clip['start'] = 0.0
                clip['end'] = duration
                clip['description'] = "Placeholder for Audio"
                
            current_time += duration

        # 2. No Visual-Only assets in AUDIO track.
        # Cleanup audio track from assets that have no sound (Images, GIFs, WebP without audio)
        sanitized_audio = []
        for a_clip in audio_track:
            asset_id = a_clip.get('asset_id')
            asset = assets_map.get(asset_id)
            
            # If asset type is image, it definitely has no audio
            if asset and asset.get('type') == 'image':
                print(f"[Sanitizer] Removing visual-only asset {asset_id} from Audio track.")
                continue
            
            # If it's a video/audio, we keep it (Renderer will do final check)
            sanitized_audio.append(a_clip)
        
        # Ensure tracks exist
        timeline_data['video'] = video_track
        timeline_data['audio'] = sanitized_audio
