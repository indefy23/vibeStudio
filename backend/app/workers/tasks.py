from app.core.celery_app import celery_app
from app.agents.orchestrator import Orchestrator

@celery_app.task
def process_project(project_id: str):
    """
    Celery task to run the Orchestrator for a given project.
    """
    print(f"Task received for project: {project_id}")
    orchestrator = Orchestrator(project_id)
    orchestrator.run()
    return f"Project {project_id} processed successfully"
