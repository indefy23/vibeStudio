from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import projects
from app.core.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="VibeStudio Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router, prefix="/projects", tags=["projects"])

@app.get("/")
def read_root():
    return {"message": "VibeStudio Backend Running"}
