from dataclasses import dataclass


@dataclass
class RecomendacoesCalagem:
    parcelamento_acima_de: float | None = None
    mensagem_parcelamento: str | None = None


@dataclass
class ParametrosCalagem:
    v2_desejado: float
    prnt_padrao: float


@dataclass
class ModeloCalagem:
    parametros: ParametrosCalagem
    recomendacoes: RecomendacoesCalagem | None = None
    unidade_saida: str | None = None  # 👈 essencial
