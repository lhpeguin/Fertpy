from dataclasses import dataclass


@dataclass
class Corretivo:

    nome: str
    prnt: float
    preco: float | None = None

    def __post_init__(self):

        # =========================
        # Validação de PRNT
        # =========================
        if not isinstance(self.prnt, (int, float)):
            raise ValueError(
                f"PRNT inválido para '{self.nome}': deve ser numérico."
            )

        if self.prnt <= 0:
            raise ValueError(
                f"PRNT inválido para '{self.nome}': deve ser maior que zero."
            )

        # =========================
        # Validação de preço
        # =========================
        if self.preco is not None and self.preco < 0:
            raise ValueError(
                f"Preço inválido para '{self.nome}': não pode ser negativo."
            )
