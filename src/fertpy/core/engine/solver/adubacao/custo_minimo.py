import numpy as np

from fertpy.core.domain.fertilizante import Fertilizer
from fertpy.core.analysis.diagnostico_formulacao import gerar_diagnostico_formulacao
from fertpy.core.engine.solver.base.programacao_linear import resolver_programacao_linear
from .fonte_unica import resolver_fonte_unica


def resolver_custo_minimo(
    demanda: dict,
    fontes: list[Fertilizer],
    precos: dict,
    fretes: dict | None = None,
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
    # Normalização (engine boundary)
    # =========================
    precos = {k.lower(): v for k, v in precos.items()}

    if fretes:
        fretes = {k.lower(): v for k, v in fretes.items()}


    # =========================
    # Validação 
    # =========================
    for nutriente in nutrientes:
        if not any(nutriente in f.nutrientes for f in fontes):
            diagnostico = gerar_diagnostico_formulacao(demanda, fontes)
            raise ValueError(
                f"Nenhuma fonte fornece o nutriente '{nutriente}'.\n\n{diagnostico}"
            )

    for f in fontes:
        nome = f.nome.lower()

        if f.nome not in precos:
            raise ValueError(f"Preço não informado para a fonte: {f.nome}")

        if precos[f.nome] <= 0:
            raise ValueError(f"Preço inválido para {f.nome}: deve ser > 0")

    # =========================
    # Validação de frete
    # =========================
    if fretes:
        for nome, valor in fretes.items():
            if valor < 0:
                raise ValueError(f"Frete inválido para {nome}: deve ser >= 0")

    # =========================
    # Matriz (A)
    # =========================
    A = np.array([
        [f.nutrientes.get(n, 0) / 100 for f in fontes]
        for n in nutrientes
    ], dtype=float)

    # =========================
    # Vetor demanda (b)
    # =========================
    b = np.array([demanda[n] for n in nutrientes], dtype=float)

    # =========================
    # Função de custo REAL
    # =========================
    def custo_unitario(nome_fonte: str) -> float:
        nome_fonte = nome_fonte.lower()
        preco = precos[nome_fonte] / 1000  # ton → kg
        frete = (fretes.get(nome_fonte, 0) / 1000) if fretes else 0
        return preco + frete

    # =========================
    # Vetor de custo
    # =========================
    epsilon = 1e-6

    c = np.array([
        custo_unitario(fonte.nome) + epsilon * (i + 1)
        for i, fonte in enumerate(fontes)
    ], dtype=float)

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
            precos=precos,
            fretes=fretes,
            tolerancia=tolerancia,
            tol_inf=tol_inf,
            tol_sup=tol_sup
        )

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
        diagnostico = gerar_diagnostico_formulacao(demanda, fontes)
        raise ValueError(f"{str(e)}\n\n{diagnostico}")

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
        "unidade": "kg/ha",
        "custo_total": float(custo_total),
        "custo_por_fonte": custo_por_fonte
    }
