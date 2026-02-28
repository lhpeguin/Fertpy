from dataclasses import dataclass


@dataclass(frozen=True)
class Classe:
    nome: str
    tipo: str = "faixa" 
    descricao: str | None = None
