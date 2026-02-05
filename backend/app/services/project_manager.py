import os
import shutil
import json
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import Session
from fastapi import UploadFile

from app.core.config import settings
from app.schemas.manifest import ProjectManifest, Asset, ProjectStages, ProjectStatus, AssetType
from app.models.sql_models import ProjectModel, AssetModel

class ProjectManager:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, name: str, instruction: str, files: list[UploadFile]) -> ProjectManifest:
        project_id = str(uuid4())
        project_dir = os.path.join(settings.STORAGE_PATH, project_id)
        assets_dir = os.path.join(project_dir, "assets")
        
        os.makedirs(assets_dir, exist_ok=True)

        assets_list = []
        db_assets = []

        for file in files:
            file_ext = os.path.splitext(file.filename)[1].lower()
            asset_type = AssetType.VIDEO # Default, simple detection logic below
            if file_ext in ['.jpg', '.png', '.jpeg', '.gif']:
                asset_type = AssetType.IMAGE
            elif file_ext in ['.mp3', '.wav']:
                asset_type = AssetType.AUDIO
            
            # Save file
            file_path = os.path.join(assets_dir, file.filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            asset_id = str(uuid4())
            asset_obj = Asset(
                id=asset_id,
                type=asset_type,
                path=file_path, # Storing absolute or relative path? using absolute for simplicity in backend
                metadata={}
            )
            assets_list.append(asset_obj)
            
            db_assets.append(AssetModel(
                id=asset_id,
                project_id=project_id,
                type=asset_type.value,
                path=file_path
            ))

        # Create Manifest
        manifest = ProjectManifest(
            project_id=project_id,
            name=name,
            instruction=instruction,
            created_at=datetime.utcnow(),
            assets=assets_list,
            stages=ProjectStages(),
            status=ProjectStatus.PENDING
        )

        manifest_path = os.path.join(project_dir, "manifest.json")
        with open(manifest_path, "w") as f:
            f.write(manifest.model_dump_json(indent=2))

        # Save to DB
        db_project = ProjectModel(
            id=project_id,
            name=name,
            status="pending",
            manifest_path=manifest_path
        )
        self.db.add(db_project)
        for da in db_assets:
            self.db.add(da)
        self.db.commit()
        self.db.refresh(db_project)

        return manifest

    def get_project_manifest(self, project_id: str) -> ProjectManifest:
        # Load from filesystem as source of truth for Agente updates
        project_dir = os.path.join(settings.STORAGE_PATH, project_id)
        manifest_path = os.path.join(project_dir, "manifest.json")
        
        if not os.path.exists(manifest_path):
            raise FileNotFoundError("Project manifest not found")
            
        with open(manifest_path, "r") as f:
            data = json.load(f)
            return ProjectManifest(**data)
