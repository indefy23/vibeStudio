from typing import Dict, Union, List, Any
import random

class DiscreteMapper:
    """
    Traduz intenções semânticas (strings) em valores numéricos discretos.
    Fonte da Verdade: concept/main.txt
    """
    
    # Ranges hardcoded conforme definido no conceito
    # "A IA não calcula valores contínuos. Ela escolhe opções discretas."
    
    RANGES = {
        "position": (0.0, 1.0),
        "scale": (0.8, 1.15),
        "opacity": (0.0, 1.0),
        "brightness": (-0.05, 0.05),
        "saturation": (0.9, 1.1)
    }

    # Tabela de mapeamento semântico
    SEMANTIC_MAP = {
        "scale": {
            "zoom_leve": (1.05, 1.12),
            "zoom_medio": (1.15, 1.25), 
            "zoom_impacto": (1.3, 1.5),
            "normal": (1.0, 1.0)
        },
        "duration": {
            "entrada_rapida": (0.2, 0.3),
            "entrada_suave": (0.5, 0.8),
            "cut_rapido": (0.8, 1.4)
        },
         "motion": {
            "stomp_discreto": {
                "keyframes_count": 2, 
                "duration_range": (0.1, 0.2), 
                "scale_bump": 0.05
            }
        }
    }

    @staticmethod
    def map_value(property_name: str, semantic_key: str) -> Union[float, Dict[str, Any]]:
        """
        Retorna um valor concreto a partir de uma chave semântica.
        Se o mapeamento definir um range, retorna um valor determinístico (ou random controlado).
        """
        mapping = DiscreteMapper.SEMANTIC_MAP.get(property_name)
        if not mapping:
             raise ValueError(f"Propriedade '{property_name}' não possui mapa semântico.")
        
        value_def = mapping.get(semantic_key)
        if value_def is None:
             raise ValueError(f"Chave '{semantic_key}' não encontrada para '{property_name}'.")

        # Se for tupla, assume range (min, max) e retorna média ou random controlado.
        # Por enquanto, retornaremos a opção mais conservadora (média) para determinismo simples,
        # ou se o contexto pedir, podemos implementar seeds.
        if isinstance(value_def, tuple) and len(value_def) == 2:
            return round((value_def[0] + value_def[1]) / 2, 3)
        
        return value_def

    @staticmethod
    def get_safe_range(property_name: str):
        return DiscreteMapper.RANGES.get(property_name)
