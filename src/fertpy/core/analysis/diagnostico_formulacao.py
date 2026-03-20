from fertpy.core.domain.fertilizante import Fertilizer
from fertpy.core.analysis.proporcao import (
    calcular_proporcao_fonte,
    formatar_proporcao,
    proporcao_inteira_demanda
)
from fertpy.core.analysis.nutriente_limitante import identificar_nutriente_limitante


def gerar_diagnostico_formulacao(
    demanda: dict[str, float],
    fontes: list[Fertilizer],
) -> str:
    """
    Gera um diagnóstico agronômico quando não é possível formular
    um fertilizante com as fontes fornecidas.
    """

    linhas = []

    linhas.append("Diagnóstico agronômico\n")

    #======================
    # Proporção da demanda
    #======================

    proporcao_demanda = proporcao_inteira_demanda(demanda)
    proporcao_demanda_str = formatar_proporcao(proporcao_demanda)

    linhas.append("Demanda:")
    linhas.append(f"N:P2O5:K2O = {proporcao_demanda_str}\n")

    #======================
    # Fontes disponíveis
    #======================-

    linhas.append("Fontes disponíveis:\n")

    for fonte in fontes:

        proporcao_fonte = calcular_proporcao_fonte(fonte.nutrientes)
        proporcao_fonte_str = formatar_proporcao(proporcao_fonte)

        linhas.append(
            f"{fonte.nome} → {proporcao_fonte_str}"
        )

    linhas.append("")

    #======================
    # Nutriente limitante
    #======================

    nutriente_limitante = identificar_nutriente_limitante(
        demanda,
        fontes,
    )

    if nutriente_limitante:

        outros = [
            n for n in demanda.keys()
            if n != nutriente_limitante
        ]

        excesso = " e ".join(outros)

        linhas.append("Problema:")
        linhas.append(
            f"Excesso de {excesso} para atender {nutriente_limitante}.\n"
        )

    #======================
    # Sugestões
    #======================

    linhas.append("Sugestões:")

    sugestoes = {
        "N": "adicionar fonte nitrogenada (ex: ureia)",
        "P2O5": "adicionar fonte fosfatada",
        "K2O": "adicionar fonte potássica",
    }

    if nutriente_limitante in sugestoes:
        linhas.append(f"• {sugestoes[nutriente_limitante]}")

    linhas.append(
        "• utilizar formulação NPK com proporção próxima da demanda"
    )

    return "\n".join(linhas)
