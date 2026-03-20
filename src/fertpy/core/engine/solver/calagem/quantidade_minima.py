import numpy as np

from fertpy.core.engine.solver.base.programacao_linear import resolver_programacao_linear
from fertpy.core.engine.calculo_calagem import CalagemEngine


def resolver_quantidade_minima_calagem(
    V_atual: float,
    V_desejado: float,
    CTC: float,
    fontes: list,
    tolerancia: float | None = 0.05,
    tol_inf: float | None = None,
    tol_sup: float | None = None
) -> dict:

    if not fontes:
        raise ValueError("Nenhuma fonte de corretivo fornecida")

    if V_desejado <= V_atual:
        raise ValueError("V% desejado deve ser maior que o atual")

    if CTC <= 0:
        raise ValueError("CTC deve ser maior que zero")

    # =========================
    # Necessidade de calagem (PRNT 100%)
    # =========================
    NC = CalagemEngine.calcular_nc_base(
        v1=V_atual,
        ctc=CTC,
        v2=V_desejado
    )

    if NC <= 0:
        return {
            "doses": {},
            "unidade": "t/ha"
        }

    # =========================
    # Matriz (A) → PRNT das fontes
    # =========================
    A = np.array([
        [fonte.prnt / 100 for fonte in fontes]
    ], dtype=float)

    # =========================
    # Vetor demanda (b)
    # =========================
    b = np.array([NC], dtype=float)

    # =========================
    # Função objetivo (c)
    # minimizar quantidade total
    # =========================
    c = np.ones(len(fontes), dtype=float)

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

    for fonte, quantidade in zip(fontes, quantidades):
        if quantidade > 1e-6:
            resultado[fonte.nome] = float(quantidade)

    return {
        "doses": resultado,
        "unidade": "t/ha"
    }
