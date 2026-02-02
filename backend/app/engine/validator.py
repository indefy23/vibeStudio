from app.models.edition import Edition, Keyframe, Track
from app.engine.mapper import DiscreteMapper

class InvariantValidator:
    """
    Garante que o Edition JSON respeite as regras inquebráveis do sistema.
    Baseado na Seção 3 do Concept: "Regras fixas que a IA não pode quebrar".
    """
    
    def validate(self, edition: Edition) -> bool:
        """
        Varre o objeto Edition procurando por violações de limites.
        Levanta ValueError se encontrar algo errado.
        Retorna True se passar.
        """
        self._validate_timeline_structure(edition)
        self._validate_ranges(edition)
        return True

    def _validate_timeline_structure(self, edition: Edition):
        # Exemplo: Clips não podem ter duração negativa
        for track in edition.timeline.tracks:
            for clip in track.clips:
                if clip.end <= clip.start:
                    raise ValueError(f"Clip {clip.id or 'unnamed'} tem duração negativa ou zero: {clip.start} -> {clip.end}")
                
                # In/Out points validação básica
                if clip.out_point <= clip.in_point:
                     raise ValueError(f"Clip {clip.id} tem in/out inválido.")

    def _validate_ranges(self, edition: Edition):
        # Valida propriedades estáticas e keyframes
        ranges = DiscreteMapper.RANGES
        
        for track in edition.timeline.tracks:
            for clip in track.clips:
                self._check_property(clip.properties.scale, ranges["scale"], f"Clip {clip.asset_id} scale")
                self._check_property(clip.properties.opacity, ranges["opacity"], f"Clip {clip.asset_id} opacity")
                
                # TODO: Validar posição {x, y}
                
                # Validar Keyframes
                for prop, keyframes in clip.keyframes.items():
                    if prop in ranges:
                        for kf in keyframes:
                             self._check_property(kf.v, ranges[prop], f"Keyframe {prop} at {kf.t}")

    def _check_property(self, value, limit_range, context_msg):
        if value is None: 
            return
            
        min_val, max_val = limit_range
        
        # Se for lista (ex: posição ou cor as vezes), precisaria iterar. 
        # Aqui assumimos float simples por enquanto.
        if isinstance(value, (int, float)):
            if not (min_val <= value <= max_val):
                raise ValueError(f"Violação de Invariante em {context_msg}: Valor {value} fora do range [{min_val}, {max_val}]")
