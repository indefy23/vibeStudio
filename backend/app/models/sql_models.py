from sqlalchemy import Column, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.core.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class ProjectModel(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pending")
    manifest_path = Column(String)
    
    # Simple relationship to track assets if needed in DB, 
    # though strict truth is in manifest.json for this architecture.
    assets = relationship("AssetModel", back_populates="project")

class AssetModel(Base):
    __tablename__ = "assets"

    id = Column(String, primary_key=True, default=generate_uuid)
    project_id = Column(String, ForeignKey("projects.id"))
    type = Column(String)
    path = Column(String)
    metadata_json = Column(JSON, default={})

    project = relationship("ProjectModel", back_populates="assets")
