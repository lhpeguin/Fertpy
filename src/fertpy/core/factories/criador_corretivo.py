from fertpy.core.domain.corretivo_solo import Corretivo


def criar_corretivo(nome: str, dados: dict) -> Corretivo:
    """
    Cria um objeto Corretivo a partir de dados estruturados.

    Espera:
    {
        "garantias": {
            "prnt": float
        }
    }
    """

    if "garantias" not in dados:
        raise ValueError(
            f"O corretivo '{nome}' não possui 'garantias'. "
            "Formato esperado: {'garantias': {'prnt': ...}}"
        )

    garantias = dados["garantias"]

    if not isinstance(garantias, dict) or not garantias:
        raise ValueError(
            f"Garantias inválidas para '{nome}'. Deve ser um dicionário não vazio."
        )

    # NORMALIZAÇÃO
    garantias = {k.lower(): v for k, v in garantias.items()}

    if "prnt" not in garantias:
        raise ValueError(
            f"O corretivo '{nome}' deve possuir 'prnt'."
        )

    if not isinstance(garantias, dict) or not garantias:
        raise ValueError(
            f"Garantias inválidas para '{nome}'. Deve ser um dicionário não vazio."
        )

    if "prnt" not in garantias:
        raise ValueError(
            f"O corretivo '{nome}' deve possuir 'prnt'."
        )

    return Corretivo(
        nome=nome,
        prnt=garantias["prnt"]
    )
