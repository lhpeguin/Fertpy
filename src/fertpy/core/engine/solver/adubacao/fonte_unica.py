import numpy as np

from fertpy.core.domain.fertilizante import Fertilizer
from fertpy.core.analysis.diagnostico_formulacao import gerar_diagnostico_formulacao


def resolver_fonte_unica(
    demanda: dict,
    fontes: list[Fertilizer],
    precos: dict | None = None,
    fretes: dict | None = None,
    tolerancia: float | None = 0.05,
    tol_inf: float | None = None,
    tol_sup: float | None = None,
) -> dict:
    """
    Seleciona a melhor fonte única que atende a demanda de nutrientes,
    minimizando o excesso relativo.

    Estratégia:
        - Para cada fonte:
            - calcula a dose necessária para atender o nutriente limitante
            - calcula excesso nos demais nutrientes
        - escolhe a fonte com menor excesso total

    Retorna:
        dict com doses, custo_total e custo_por_fonte (se aplicável)
    """

    if not demanda:
        raise ValueError("A demanda de nutrientes não pode estar vazia")

    if not fontes:
        raise ValueError("Nenhuma fonte de fertilizante fornecida")

    nutrientes = list(demanda.keys())

    # =========================
    # Normalização de tolerância
    # =========================
    if tol_inf is None and tol_sup is None:
        tol_inf = 0.0
        tol_sup = tolerancia if tolerancia is not None else 0.05
    else:
        tol_inf = 0.0 if tol_inf is None else tol_inf
        tol_sup = 0.0 if tol_sup is None else tol_sup

    melhor_resultado = None
    melhor_score = float("inf")

    # =========================
    # Função de custo (opcional)
    # =========================
    def custo_unitario(nome_fonte: str) -> float:
        if precos is None:
            return 0.0

        preco = precos.get(nome_fonte)
        if preco is None:
            raise ValueError(f"Preço não informado para a fonte: {nome_fonte}")

        frete = (fretes.get(nome_fonte, 0) if fretes else 0)

        return (preco + frete) / 1000  # ton → kg

    # =========================
    # Avaliar cada fonte
    # =========================
    for fonte in fontes:

        garantias = fonte.nutrientes

        # fonte não fornece algum nutriente → descarta
        if any(n not in garantias or garantias[n] <= 0 for n in nutrientes):
            continue

        # =========================
        # Calcular dose necessária
        # =========================
        doses_necessarias = []

        for n in nutrientes:
            teor = garantias[n] / 100
            doses_necessarias.append(demanda[n] / teor)

        dose = max(doses_necessarias)

        # =========================
        # Calcular excesso
        # =========================
        valido = True
        excesso_total = 0.0

        for n in nutrientes:
            teor = garantias[n] / 100
            fornecido = dose * teor

            demanda_n = demanda[n]

            limite_min = demanda_n * (1 - tol_inf)
            limite_max = demanda_n * (1 + tol_sup)

            # Não atende mínimo (só ocorre se tol_inf > 0)
            if fornecido < limite_min:
                valido = False
                break

            # Excesso acima do permitido
            if fornecido > limite_max:
                valido = False
                break

            # excesso dentro da tolerância → penaliza suavemente
            excesso = max(0.0, fornecido - demanda_n)
            excesso_rel = excesso / demanda_n if demanda_n > 0 else 0

            # penalização quadrática
            excesso_total += excesso_rel ** 2

        if not valido:
            continue

        # =========================
        # Critério de escolha
        # =========================
        score = excesso_total

        # opcional: incluir custo no critério
        if precos is not None:
            score += 1e-3 * dose * custo_unitario(fonte.nome)

        if (
            score < melhor_score or
            (
                np.isclose(score, melhor_score) and
                (melhor_resultado is None or dose < list(melhor_resultado["doses"].values())[0])
            )
        ):
            melhor_score = score

            custo_total = None
            custo_por_fonte = {}

            if precos is not None:
                custo = dose * custo_unitario(fonte.nome)
                custo_total = float(custo)
                custo_por_fonte = {fonte.nome: float(custo)}

            melhor_resultado = {
                "doses": {fonte.nome: float(dose)},
                "unidade": "kg/ha",
                "custo_total": custo_total,
                "custo_por_fonte": custo_por_fonte,
            }

    # =========================
    # Nenhuma fonte válida
    # =========================
    if melhor_resultado is None:
        diagnostico = gerar_diagnostico_formulacao(demanda, fontes)
        raise ValueError(
            "Nenhuma fonte única consegue atender a demanda de nutrientes.\n\n"
            f"{diagnostico}"
        )

    return melhor_resultado
