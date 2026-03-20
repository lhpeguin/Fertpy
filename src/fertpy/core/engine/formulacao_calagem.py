from fertpy.core.engine.solver.calagem.quantidade_minima import resolver_quantidade_minima_calagem
from fertpy.core.engine.solver.calagem.custo_minimo import resolver_custo_minimo_calagem


SOLVERS = {
    "quantidade_minima": resolver_quantidade_minima_calagem,
    "custo_minimo": resolver_custo_minimo_calagem
}


def formular_calagem(
    V_atual: float,
    V_desejado: float,
    CTC: float,
    fontes: list,
    precos: dict | None = None,
    fretes: dict | None = None,
    solver: str = "quantidade_minima",
    tolerancia: float = 0.05,
    tol_inf: float | None = None,
    tol_sup: float | None = None,
    modelo=None
) -> dict:

    # ====================
    # Validações básicas
    # ====================
    if not fontes:
        raise ValueError("Nenhuma fonte de corretivo fornecida")

    if V_desejado <= V_atual:
        raise ValueError("V% desejado deve ser maior que o atual")

    if CTC <= 0:
        raise ValueError("CTC deve ser maior que zero")

    if not (0 <= tolerancia <= 1):
        raise ValueError("Tolerancia deve estar entre 0 e 1")

    if solver not in SOLVERS:
        raise ValueError(f"Solver desconhecido: {solver}")

    # ====================
    # Seleção do solver
    # ====================
    solver_fn = SOLVERS[solver]

    # ====================
    # Montar argumentos
    # ====================
    kwargs = {
        "V_atual": V_atual,
        "V_desejado": V_desejado,
        "CTC": CTC,
        "fontes": fontes,
        "tolerancia": tolerancia,
        "tol_inf": tol_inf,
        "tol_sup": tol_sup
    }


    if solver == "custo_minimo":
        if precos is None:
            raise ValueError(
                "O solver 'custo_minimo' requer um dicionário de preços"
            )
        
        kwargs["precos"] = precos
        kwargs["fretes"] = fretes

    # ====================
    # Execução
    # ====================
    resultado = solver_fn(**kwargs)

    doses = resultado.get("doses", {})

    observacoes = []

    if modelo and getattr(modelo, "recomendacoes", None):
        rec = modelo.recomendacoes
        dose_total = sum(doses.values())

        if (
            rec.parcelamento_acima_de
            and dose_total > rec.parcelamento_acima_de
        ):
            observacoes.append(rec.mensagem_parcelamento)

    return {
        "doses": doses,
        "observacoes": observacoes,
        "custo_total": resultado.get("custo_total"),
        "custo_por_fonte": resultado.get("custo_por_fonte") or {}
    }
