import numpy as np

from fertpy.core.domain.fertilizante import Fertilizer
from fertpy.core.analysis.diagnostico_formulacao import gerar_diagnostico_formulacao
from fertpy.core.engine.solver.base.programacao_linear import resolver_programacao_linear
from .fonte_unica import resolver_fonte_unica


def resolver_quantidade_minima(
    demanda: dict,
    fontes: list[Fertilizer],
    tolerancia: float | None = 0.05,
    tol_inf: float | None = None,
    tol_sup: float | None = None,
    modo: str = "mistura"
) -> dict:

    if not demanda:
        raise ValueError("A demanda de nutrientes não pode estar vazia")

    if not fontes:
        raise ValueError("Nenhuma fonte de fertilizante fornecida")

    nutrientes = list(demanda.keys())

    # =========================
    # Validação ANTES do solver
    # =========================
    for nutriente in nutrientes:
        if not any(nutriente in f.nutrientes for f in fontes):
            diagnostico = gerar_diagnostico_formulacao(demanda, fontes)
            raise ValueError(
                f"Nenhuma fonte fornece o nutriente '{nutriente}'.\n\n{diagnostico}"
            )

    # =========================
    # Montagem da matriz (A)
    # =========================
    A = np.array([
        [f.nutrientes.get(n, 0) / 100 for f in fontes]
        for n in nutrientes
    ], dtype=float)

    # =========================
    # Vetor de demanda (b)
    # =========================
    b = np.array([demanda[n] for n in nutrientes], dtype=float)

    # =========================
    # Função objetivo (c)
    # minimizar quantidade total
    # =========================
    c = np.ones(len(fontes), dtype=float)

    # =========================
    # Validação de modo
    # =========================
    if modo not in ("mistura", "fonte_unica"):
        raise ValueError(f"Modo inválido: {modo}")

    # =========================
    # MODO: fonte única
    # =========================
    if modo == "fonte_unica":
        return resolver_fonte_unica(
            demanda=demanda,
            fontes=fontes,
            precos=None,
            fretes=None,
            tolerancia=tolerancia,
            tol_inf=tol_inf,
            tol_sup=tol_sup
        )

    # =========================
    # Solver base
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
        diagnostico = gerar_diagnostico_formulacao(demanda, fontes)
        raise ValueError(f"{str(e)}\n\n{diagnostico}")

    # =========================
    # Pós-processamento
    # =========================
    resultado = {}

    for fonte, quantidade in zip(fontes, quantidades):
        if quantidade > 1e-6:
            resultado[fonte.nome] = float(quantidade)

    return {
        "doses": resultado,
        "unidade": "kg/ha"
    }
