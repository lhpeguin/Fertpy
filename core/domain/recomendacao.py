from dataclasses import dataclass

from fertpy.core.domain.intervalo import Intervalo
from fertpy.core.domain.classe import Classe


@dataclass(frozen=True)
class Recomendacao:
    nutriente: str
    
    dose: float | Intervalo | str
    unidade: str

    classe: Classe

    observacoes: list[str] | None = None
    fonte: dict | None = None

    def __post_init__(self):

        if not self.nutriente:
            raise ValueError("Recomendação precisa do parâmetro nutriente")
        
        if not self.unidade:
            raise ValueError("Recomendação precisa do parâmetro unidade")
