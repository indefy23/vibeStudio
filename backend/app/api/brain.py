from fastapi import APIRouter, HTTPException
from app.models.plan import EditPlan
from app.models.edition import Edition, Asset, Assets
from app.engine.transformer import PlanTransformer
import random

router = APIRouter()

# Mock Assets Database
MOCK_ASSETS = Assets(
    video=[
        Asset(id="v1", src="/mock_video_1.mp4", metadata={"duration": 5.0}),
        Asset(id="v2", src="/mock_video_2.mp4", metadata={"duration": 8.0}),
        Asset(id="v3", src="/mock_video_3.mp4", metadata={"duration": 4.5}),
    ]
)

@router.post("/generate", response_model=Edition)
async def generate_edition(prompt: str):
    """
    Simula o fluxo completo: LLM (Mock) -> Plan -> Transformer -> Edition JSON.
    """
    print(f"Recebido prompt: {prompt}")
    
    # 1. Simular IA gerando o Plano (Brain Mock)
    # Em produção, aqui chamaria o GPT/Gemini para preencher o EditPlan
    plan = EditPlan(
        goal=prompt,
        duration_target=10.0, # Fixo para teste
        pacing={"cut_style": "rapido" if "rapido" in prompt else "dinamico"},
        visual_policy={"zoom_usage": "medio" if "zoom" in prompt else "leve"}
    )
    
    # 2. Transformar Plano em JSON Executável
    transformer = PlanTransformer()
    edition = transformer.transform(plan, MOCK_ASSETS)
    
    return edition

@router.post("/refine", response_model=Edition)
async def refine_edition(current_edition: Edition, instruction: str):
    """
    Refina uma edição existente. (Placeholder)
    """
    # Lógica de Patching viria aqui
    return current_edition
