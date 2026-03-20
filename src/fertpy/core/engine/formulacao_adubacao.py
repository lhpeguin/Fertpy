from fertpy.core.domain.fertilizante import Fertilizer
from fertpy.core.engine.solver.adubacao.custo_minimo import resolver_custo_minimo
from fertpy.core.engine.solver.adubacao.quantidade_minima import resolver_quantidade_minima

SOLVERS = {
    "quantidade_minima": resolver_quantidade_minima,
    "custo_minimo": resolver_custo_minimo
}


def formular(
        demanda: dict,
        fontes: list[Fertilizer],
        precos: dict | None = None,
        fretes: dict | None = None,
        solver: str = "quantidade_minima",
        tolerancia: float | None = 0.05,
        tol_inf: float | None = None,
        tol_sup: float | None = None,
        modo: str = "mistura"
) -> dict:

    # ====================
    # Validações básicas
    # ====================
    if not demanda:
        raise ValueError("A demanda de nutrientes não pode estar vazia")

    if not fontes:
        raise ValueError("Nenhuma fonte de fertilizante fornecida")

    if tolerancia is not None and not (0 <= tolerancia < 1):
        raise ValueError("tolerancia deve estar entre 0 e 1")

    if tol_inf is not None and not (0 <= tol_inf < 1):
        raise ValueError("tol_inf deve estar entre 0 e 1")

    if tol_sup is not None and tol_sup < 0:
        raise ValueError("tol_sup deve ser >= 0")

    if solver not in SOLVERS:
        raise ValueError(f"Solver desconhecido: {solver}")
    
    if modo not in {"mistura", "fonte_unica"}:
        raise ValueError(f"Modo desconhecido: {modo}")

    # ====================
    # Seleção do solver
    # ====================
    solver_fn = SOLVERS[solver]

    # ====================
    # Regra de precedência
    # ====================
    if tol_inf is None and tol_sup is None:
        tol_inf_final = 0
        tol_sup_final = tolerancia
    else:
        tol_inf_final = 0.0 if tol_inf is None else tol_inf
        tol_sup_final = 0.0 if tol_sup is None else tol_sup

    # ====================
    # Montar argumentos
    # ====================
    kwargs = {
        "demanda": demanda,
        "fontes": fontes,
        "tolerancia": tolerancia,
        "tol_inf": tol_inf_final,
        "tol_sup": tol_sup_final,
        "modo": modo
    }

    if solver == "custo_minimo":
        if precos is None:
            raise ValueError(
                "O solver 'custo_minimo' requer um dicionario de preços"
            )

        kwargs["precos"] = precos
        kwargs["fretes"] = fretes

    # ====================
    # Execução
    # ====================
    resultado = solver_fn(**kwargs)

    return {
        "doses": resultado.get("doses", {}),
        "unidade": resultado.get("unidade", "kg/ha"),
        "observacoes": resultado.get("observacoes", []),
        "custo_total": resultado.get("custo_total"),
        "custo_por_fonte": resultado.get("custo_por_fonte") or {}
    }
