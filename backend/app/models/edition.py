from typing import List, Dict, Optional, Literal, Union, Any
from pydantic import BaseModel, Field

# --- Primitives & Enums ---

InterpolationType = Literal["linear", "ease-in", "ease-out", "step"]
AssetType = Literal["video", "image", "audio"]
TrackType = Literal["video", "audio", "overlay"]
AnchorType = Literal["center", "top-left", "top-right", "bottom-left", "bottom-right"]

# --- Keyframes & Properties ---

class Keyframe(BaseModel):
    t: float = Field(..., description="Timestamp relativo ao início do clip/efeito")
    v: Union[float, int, List[float]] = Field(..., description="Valor na timeline")
    e: InterpolationType = Field("linear", description="Tipo de interpolação")

class Properties(BaseModel):
    anchor: Optional[AnchorType] = "center"
    position: Optional[Dict[str, float]] = Field(default_factory=lambda: {"x": 0.5, "y": 0.5})
    scale: Optional[float] = 1.0
    opacity: Optional[float] = 1.0
    rotation: Optional[float] = 0.0
    volume: Optional[float] = 1.0
    # Permite propriedades extras dinâmicas (ex: text specific)
    extra: Dict[str, Any] = Field(default_factory=dict) 

# --- Assets ---

class Asset(BaseModel):
    id: str
    src: str
    type: AssetType = "video"
    metadata: Dict[str, Any] = Field(default_factory=dict)

class Assets(BaseModel):
    video: List[Asset] = Field(default_factory=list)
    audio: List[Asset] = Field(default_factory=list)
    image: List[Asset] = Field(default_factory=list)

# --- Timeline Elements ---

class Clip(BaseModel):
    id: Optional[str] = None
    asset_id: str = Field(..., alias="asset")
    start: float = Field(..., description="Inicio na timeline global")
    end: float = Field(..., description="Fim na timeline global")
    in_point: float = Field(0.0, alias="in", description="Ponto de corte inicial no asset")
    out_point: float = Field(..., alias="out", description="Ponto de corte final no asset")
    
    properties: Properties = Field(default_factory=Properties)
    keyframes: Dict[str, List[Keyframe]] = Field(default_factory=dict)

class OverlayElement(BaseModel):
    id: str
    type: Literal["text", "shape", "image"]
    content: Optional[str] = None # Para texto ou path
    start: float
    end: float
    properties: Properties = Field(default_factory=Properties)
    keyframes: Dict[str, List[Keyframe]] = Field(default_factory=dict)

# --- Tracks ---

class Track(BaseModel):
    id: str
    type: TrackType
    clips: List[Clip] = Field(default_factory=list)
    elements: List[OverlayElement] = Field(default_factory=list)

# --- Root ---

class Timeline(BaseModel):
    tracks: List[Track]

class Meta(BaseModel):
    version: str = "1.0"
    fps: int = 30
    format: str = "9:16" # TODO: Validar formatos ex: "1920x1080" ou enum
    duration: float

class Adjustments(BaseModel):
    color: Dict[str, List[Keyframe]] = Field(default_factory=dict)
    audio: Dict[str, List[Keyframe]] = Field(default_factory=dict)

class Edition(BaseModel):
    meta: Meta
    assets: Assets
    timeline: Timeline
    adjustments: Optional[Adjustments] = Field(default_factory=Adjustments)

    class Config:
        populate_by_name = True
