from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Form
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.project_manager import ProjectManager
from app.schemas.manifest import ProjectManifest, ProjectCreateRequest
from app.core.celery_app import celery_app

router = APIRouter()

@router.post("/", response_model=ProjectManifest)
def create_project(
    name: str = Form(...),
    instruction: str = Form("Create a summary."),
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db)
):
    manager = ProjectManager(db)
    manifest = manager.create_project(name, instruction, files)
    
    # Enqueue processing task
    # Using send_task to decouple from worker implementation (which isn't fully ready/imported yet)
    celery_app.send_task("app.workers.tasks.process_project", args=[manifest.project_id])
    
    return manifest

@router.get("/{project_id}", response_model=ProjectManifest)
def get_project(project_id: str, db: Session = Depends(get_db)):
    manager = ProjectManager(db)
    try:
        return manager.get_project_manifest(project_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Project not found")
