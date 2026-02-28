from dataclasses import dataclass

from fertpy.core.domain.criterio import Criterio


@dataclass(frozen=True)
class ModeloAgronomico:
    nutriente: str
    unidade_saida: str

    criterios: list[Criterio]

    nutriente_recomendado: str | None = None
    unidade_entrada: str | None = None
    metodo_analitico: str | None = None
    fonte_referencia: dict | None = None

    def __post_init__(self):

        if not self.nutriente:
            raise ValueError("O modelo não possui nutriente declarado")
        
        if not self.unidade_saida:
            raise ValueError("O modelo não possui unidade de saida declarado") 

        if not self.criterios:
            raise ValueError("Modelo precisa de critérios")

        for c in self.criterios:
            if not isinstance(c, Criterio):
                raise TypeError("Todos os critérios devem ser instâncias de criterio")
