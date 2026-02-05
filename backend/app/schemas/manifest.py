from typing import List, Optional, Dict, Any
from enum import Enum
from pydantic import BaseModel
from datetime import datetime
import uuid

class AssetType(str, Enum):
    VIDEO = "video"
    AUDIO = "audio"
    IMAGE = "image"

class Asset(BaseModel):
    id: str
    type: AssetType
    path: str
    metadata: Optional[Dict[str, Any]] = {} # Duration, resolution, visual analysis

class ProjectStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    ERROR = "error"

class ProjectStages(BaseModel):
    analysis: Optional[str] = "context.json"
    editing: Optional[str] = "timeline.json"
    rendering: Optional[str] = "final_video.mp4"

class ProjectManifest(BaseModel):
    project_id: str
    name: str
    instruction: Optional[str] = "Create a summary of the video."
    created_at: datetime
    assets: List[Asset]
    stages: ProjectStages
    current_stage: str = "pending"
    status: ProjectStatus = ProjectStatus.PENDING

    class Config:
        from_attributes = True

# Request Schemas
class ProjectCreateRequest(BaseModel):
    name: str
    instruction: str
