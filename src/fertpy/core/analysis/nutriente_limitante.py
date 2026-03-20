from fertpy.core.domain.fertilizante import Fertilizer


def identificar_nutriente_limitante(
    demanda: dict[str, float],
    fontes: list[Fertilizer],
) -> str | None:
    """
    Identifica qual nutriente força a aplicação excessiva dos demais.

    Estratégia:
    - Para cada nutriente da demanda
    - Calculamos quanto de fertilizante seria necessário para atendê-lo
    - O nutriente que exigir MAIS fertilizante tende a causar excesso
      dos outros nutrientes.

    Retorna:
        nome do nutriente limitante
        ou None se não for possível determinar
    """

    if not demanda or not fontes:
        return None

    nutrientes = list(demanda.keys())

    # usamos apenas a primeira fonte (caso típico de diagnóstico)
    fonte = fontes[0]

    fator_por_nutriente = {}

    for nutriente in nutrientes:

        teor = fonte.nutrientes.get(nutriente, 0)

        if teor <= 0:
            continue

        # quanto fertilizante seria necessário
        fator = demanda[nutriente] / (teor / 100)

        fator_por_nutriente[nutriente] = fator

    if not fator_por_nutriente:
        return None

    # o nutriente que exige mais fertilizante é o limitante
    nutriente_limitante = max(
        fator_por_nutriente,
        key=fator_por_nutriente.get
    )

    return nutriente_limitante
