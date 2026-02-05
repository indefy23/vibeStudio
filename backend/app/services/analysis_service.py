import os
import json
from app.schemas.manifest import ProjectManifest, AssetType
from app.tools.media_tools import get_video_duration, transcribe_with_openai
from app.services.llm import LLMService

class AnalysisService:
    def __init__(self, project_dir: str, manifest: ProjectManifest):
        self.project_dir = project_dir
        self.manifest = manifest
        self.llm = LLMService() # Visual Analysis

    def analyze_project(self) -> dict:
        """
        Runs all analysis steps and returns a consolidated context dict.
        Also saves intermediate JSONs.
        """
        analysis_context = {
            "project_id": self.manifest.project_id,
            "instruction": self.manifest.instruction,
            "assets_analysis": []
        }
        
        for asset in self.manifest.assets:
            print(f"Analyzing asset: {asset.id} ({asset.type})")
            
            asset_data = {
                "id": asset.id,
                "type": asset.type,
                "path": asset.path,
                "duration": 0,
                "transcription": None,
                "visual_description": None
            }
            
            # 1. Metadata (Duration) - applies to Audio/Video
            if asset.type in [AssetType.VIDEO, AssetType.AUDIO]:
                duration = get_video_duration(asset.path)
                asset_data["duration"] = duration
                
                # Update Manifest in memory (persistence handled by caller technically, but good to have)
                asset.metadata["duration"] = duration

            # 2. Transcription - applies to Audio/Video
            # 1. Metadata Extraction (Universal)
            # We probe EVERYTHING. Images might return 0, GIFs return duration, Audio returns duration.
            print(f"  - Probing metadata...")
            duration = get_video_duration(asset.path)
            asset_data["duration"] = duration
            asset.metadata["duration"] = duration
            
            # 2. Transcription (Video/Audio only)
            if asset.type in [AssetType.VIDEO, AssetType.AUDIO] and duration > 0:
                print(f"  - Transcribing...")
                transcription = transcribe_with_openai(asset.path)
                
                # Cleanup noisy segments data
                if "segments" in transcription:
                    cleaned_segments = []
                    for seg in transcription["segments"]:
                        # Keep only essential fields to save context window
                        cleaned_segments.append({
                            "id": seg.get("id"),
                            "start": seg.get("start"),
                            "end": seg.get("end"),
                            "text": seg.get("text", "").strip()
                        })
                    transcription["segments"] = cleaned_segments
                
                asset_data["transcription"] = transcription
            
            # 3. Visual Analysis
            # For IMAGE: Analyze directly
            if asset.type == AssetType.IMAGE:
                print(f"  - Visual Analysis (Image)...")
                visual = self.llm.analyze_image(asset.path)
                asset_data["visual_description"] = visual
                asset.metadata.update(visual)

            # For VIDEO: Extract a representative frame and analyze
            elif asset.type == AssetType.VIDEO:
                print(f"  - Visual Analysis (Video Frame)...")
                # Create a temp path for the frame
                frame_path = f"{asset.path}_thumb.jpg"
                timestamp = max(2.0, asset_data["duration"] * 0.1) 
                
                from app.tools.media_tools import extract_frame
                extracted_path = extract_frame(asset.path, frame_path, time=timestamp)
                
                if extracted_path and os.path.exists(extracted_path):
                    visual = self.llm.analyze_image(extracted_path)
                    asset_data["visual_description"] = visual
                    asset.metadata.update(visual)
                else:
                    print("  - Failed to extract frame for visual analysis.")

            # 4. Contextual Classification (Intelligent)
            print(f"  - Classifying (LLM)...")
            # We pass visual description as text if available, or transcription
            text_context = asset_data.get("transcription") or str(asset_data.get("visual_description", ""))
            
            classification = self.llm.classify_asset(
                filename=os.path.basename(asset.path),
                duration=asset_data["duration"],
                transcription=text_context
            )
            asset_data.update(classification)
            asset.metadata.update(classification)

            analysis_context["assets_analysis"].append(asset_data)

        return analysis_context
