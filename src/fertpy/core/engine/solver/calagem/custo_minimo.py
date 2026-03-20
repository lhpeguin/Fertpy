import numpy as np

from fertpy.core.engine.solver.base.programacao_linear import resolver_programacao_linear
from fertpy.core.engine.calculo_calagem import CalagemEngine


def resolver_custo_minimo_calagem(
    V_atual: float,
    V_desejado: float,
    CTC: float,
    fontes: list,
    precos: dict,
    fretes: dict | None = None,
    tolerancia: float | None = 0.05,
    tol_inf: float | None = None,
    tol_sup: float | None = None,
    **kwargs
) -> dict:

    if not fontes:
        raise ValueError("Nenhuma fonte de corretivo fornecida")

    if V_desejado <= V_atual:
        raise ValueError("V% desejado deve ser maior que o atual")

    if CTC <= 0:
        raise ValueError("CTC deve ser maior que zero")

    if not precos:
        raise ValueError("Preços devem ser informados")

    # =========================
    # Validação de PRNT e preço
    # =========================
    for fonte in fontes:
        if fonte.prnt is None or fonte.prnt <= 0:
            raise ValueError(f"PRNT inválido para a fonte: {fonte.nome}")

        if fonte.nome not in precos:
            raise ValueError(f"Preço não informado para a fonte: {fonte.nome}")

        if precos[fonte.nome] <= 0:
            raise ValueError(
                f"Preço inválido para {fonte.nome}: deve ser > 0"
            )

    # =========================
    # Validação de frete
    # =========================
    if fretes:
        for nome, valor in fretes.items():
            if valor < 0:
                raise ValueError(f"Frete inválido para {nome}: deve ser >= 0")

    # =========================
    # Necessidade de calagem
    # =========================
    NC = CalagemEngine.calcular_nc_base(
        v1=V_atual,
        ctc=CTC,
        v2=V_desejado
    )

    if NC <= 0:
        return {
            "doses": {},
            "unidade": "t/ha",
            "custo_total": 0.0,
            "custo_por_fonte": {}
        }

    # =========================
    # Matriz (A)
    # =========================
    A = np.array([
        [fonte.prnt / 100 for fonte in fontes]
    ], dtype=float)

    # =========================
    # Vetor (b)
    # =========================
    b = np.array([NC], dtype=float)

    # =========================
    # Função de custo REAL
    # =========================
    def custo_unitario(nome_fonte: str) -> float:
        preco = precos[nome_fonte]
        frete = fretes.get(nome_fonte, 0) if fretes else 0
        return preco + frete

    # =========================
    # Vetor de custo (com desempate)
    # =========================
    epsilon = 1e-6

    c = np.array([
        custo_unitario(fonte.nome) + epsilon * (i + 1)
        for i, fonte in enumerate(fontes)
    ], dtype=float)

    # =========================
    # Solver
    # =========================
    try:
        quantidades = resolver_programacao_linear(
            A=A,
            b=b,
            c=c,
            tolerancia=tolerancia,
            tol_inf=tol_inf,
            tol_sup=tol_sup
        )
    except ValueError as e:
        raise ValueError(f"{str(e)}\n\nFalha ao calcular calagem")

    # =========================
    # Pós-processamento
    # =========================
    resultado = {}
    custo_total = 0.0
    custo_por_fonte = {}

    for fonte, quantidade in zip(fontes, quantidades):

        if quantidade > 1e-6:

            quantidade = float(quantidade)
            resultado[fonte.nome] = quantidade

            custo = custo_unitario(fonte.nome) * quantidade
            custo_total += custo
            custo_por_fonte[fonte.nome] = custo

    return {
        "doses": resultado,
        "unidade": "t/ha",
        "custo_total": float(custo_total),
        "custo_por_fonte": custo_por_fonte
    }