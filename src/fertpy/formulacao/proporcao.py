from fertpy.core.analysis.proporcao import (
    calcular_proporcao_demanda,
    proporcao_inteira_demanda,
    formatar_proporcao,
)


def proporcao(
    n: float = 0,
    p: float = 0,
    k: float = 0,
    modo: str = "inteira",
    formatado: bool = True,
):
    """
    Orquestrador de proporção NPK.

    Parâmetros:
        n, p, k: valores de nutrientes
        modo: "inteira" ou "relativa"
        formatado: retorna string ou dict

    Exemplo:
        proporcao(80, 60, 40)
        -> "4:3:2"
    """

    demanda = {
        "N": n,
        "P2O5": p,
        "K2O": k,
    }

    if modo == "inteira":
        resultado = proporcao_inteira_demanda(demanda)
    elif modo == "relativa":
        resultado = calcular_proporcao_demanda(demanda)
    else:
        raise ValueError("modo deve ser 'inteira' ou 'relativa'")

    if formatado:
        return formatar_proporcao(resultado)

    return resultado
