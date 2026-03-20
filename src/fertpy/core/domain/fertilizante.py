from dataclasses import dataclass, field


@dataclass
class Fertilizer:

    nome: str
    nutrientes: dict[str, float] = field(default_factory=dict)
    preco: float | None = None

    def __post_init__(self):

        # =========================
        # Validação de nutrientes
        # =========================
        if not isinstance(self.nutrientes, dict) or not self.nutrientes:
            raise ValueError(
                f"Fertilizante '{self.nome}' deve ter nutrientes válidos."
            )

        for k, v in self.nutrientes.items():

            if not isinstance(k, str):
                raise ValueError(
                    f"Nutriente inválido em '{self.nome}': chave não é string."
                )

            if not isinstance(v, (int, float)):
                raise ValueError(
                    f"Valor inválido para '{k}' em '{self.nome}': deve ser numérico."
                )

            if v < 0:
                raise ValueError(
                    f"Valor negativo para '{k}' em '{self.nome}' não é permitido."
                )

        # =========================
        # Validação de preço
        # =========================
        if self.preco is not None and self.preco < 0:
            raise ValueError(
                f"Preço inválido para '{self.nome}': não pode ser negativo."
            )

    def teor(self, nutriente: str) -> float:
        return self.nutrientes.get(nutriente, 0.0)