import random
from app.models.edition import Edition, Meta, Timeline, Track, Clip, Properties, Keyframe, Assets
from app.models.plan import EditPlan
from app.engine.mapper import DiscreteMapper

class PlanTransformer:
    def transform(self, plan: EditPlan, assets: Assets) -> Edition:
        """
        Transforma deterministicamente (com seed controlada se necessário) um Plano em um Edition JSON.
        """
        # 1. Setup Meta
        meta = Meta(
            duration=plan.duration_target,
            format=plan.format,
            fps=30
        )
        
        # 2. Setup Tracks
        # Lógica simplificada: 1 track de vídeo principal, 1 de overlay
        main_track = Track(id="main_video", type="video")
        overlay_track = Track(id="overlays", type="overlay")
        
        # 3. Distribuir Assets na Timeline (Pacing)
        # Parse average duration (ex "0.8-1.4s" -> 1.1)
        # Para simplificar, usamos média fixa baseada no estilo
        avg_dur = 2.0
        if plan.pacing.cut_style == "rapido":
            avg_dur = 1.0
        
        current_time = 0.0
        asset_pool = assets.video + assets.image
        
        # Round Robin simples nos assets disponíveis
        if not asset_pool:
            print("WARN: Nenhum asset fornecido para transformar.")
        else:
            idx = 0
            while current_time < plan.duration_target:
                asset = asset_pool[idx % len(asset_pool)]
                
                # Calcular duração deste clip
                clip_dur = avg_dur
                # Ajustar para não passar do total
                if current_time + clip_dur > plan.duration_target:
                    clip_dur = plan.duration_target - current_time
                
                # Criar Clip
                clip = Clip(
                    asset=asset.id,
                    start=round(current_time, 2),
                    end=round(current_time + clip_dur, 2),
                    in_=0.0, # TODO: Detectar cenas relevantes
                    out=clip_dur
                )
                
                # Aplicar Visual Policy (Zoom/Motion) via Mapper
                self._apply_visual_styles(clip, plan)
                
                main_track.clips.append(clip)
                current_time += clip_dur
                idx += 1

        timeline = Timeline(tracks=[main_track, overlay_track])

        return Edition(
            meta=meta,
            assets=assets,
            timeline=timeline
        )

    def _apply_visual_styles(self, clip: Clip, plan: EditPlan):
        # Mapeia intenção "zoom_usage" -> scale values
        zoom_intent = f"zoom_{plan.visual_policy.zoom_usage}" # ex: zoom_leve
        
        try:
            # Tenta pegar do mapper, se falhar usa default
            scale_val = DiscreteMapper.map_value("scale", zoom_intent)
        except ValueError:
            scale_val = 1.0

        # Se for um valor estático
        if isinstance(scale_val, float):
             clip.properties.scale = scale_val
        
        # Se o estilo pede movimento (Keyframes)
        if plan.visual_policy.motion_style == "suave":
            # Exemplo: Zoom in lento (scale start -> scale start * 1.05)
            # Como Keyframe precisa de lista...
            # AQUI APLICAMOS A REGRA DE PROPRIEDADES ANIMÁVEIS
            pass
