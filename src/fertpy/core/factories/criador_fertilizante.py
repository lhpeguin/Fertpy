from fertpy.core.domain.fertilizante import Fertilizer


def criar_fertilizante(nome: str, dados: dict) -> Fertilizer:
    """
    Cria um objeto Fertilizer a partir de dados já estruturados.

    Parameters
    ----------
    nome : str
        Nome da fonte
    dados : dict
        Deve conter pelo menos:
        {
            "garantias": {
                "N": float,
                "P2O5": float,
                "K2O": float
            }
        }
    """

    if "garantias" not in dados:
        raise ValueError(
            f"A fonte '{nome}' não possui 'garantias'. "
            "Formato esperado: {'garantias': {'N': ..., 'P2O5': ..., 'K2O': ...}}"
        )

    garantias = dados["garantias"]

    if not isinstance(garantias, dict) or not garantias:
        raise ValueError(
            f"Garantias inválidas para '{nome}'. Deve ser um dicionário não vazio."
        )

    return Fertilizer(nome, garantias)