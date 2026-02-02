from typing import List, Dict, Optional, Literal, Any
from pydantic import BaseModel, Field

class Pacing(BaseModel):
    cut_style: Literal["rapido", "lento", "dinamico"] = "dinamico"
    average_shot_duration: str = Field("0.8–1.4s", description="Range em string para ser parseado depois")

class AudioUsage(BaseModel):
    speech_priority: bool = True
    sync_with_beats: bool = True

class VisualPolicy(BaseModel):
    zoom_usage: Literal["leve", "medio", "impacto", "nenhum"] = "leve"
    motion_style: Literal["stomp", "suave", "estatico"] = "suave"

class TextPolicy(BaseModel):
    use_captions: bool = True
    highlight_keywords: bool = True
    effects: List[str] = Field(default_factory=lambda: ["typewriter"])

class EditPlan(BaseModel):
    """
    Estrutura de Intenção de Alto Nível.
    A IA preenche isso primeiro. O sistema transforma em Edition JSON.
    """
    goal: str
    format: Literal["9:16", "16:9", "1:1"] = "9:16"
    duration_target: float = Field(..., description="Duração alvo em segundos")
    
    pacing: Pacing = Field(default_factory=Pacing)
    audio_usage: AudioUsage = Field(default_factory=AudioUsage)
    visual_policy: VisualPolicy = Field(default_factory=VisualPolicy)
    text_policy: TextPolicy = Field(default_factory=TextPolicy)
    
    # Lista de Assets IDs que o planejou usar (opcional, pode vir do request)
    selected_assets: List[str] = Field(default_factory=list)
