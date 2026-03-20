import numpy as np
from scipy.optimize import linprog


def resolver_programacao_linear(
    A: np.ndarray,
    b: np.ndarray,
    c: np.ndarray,
    tolerancia: float | None = 0.05,
    tol_inf: float | None = None,
    tol_sup: float | None = None
) -> np.ndarray:
    """
    Resolve um problema de programação linear do tipo:

        min c^T x

    sujeito a:

        b * (1 - tol_inf) <= A x <= b * (1 + tol_sup)
        x >= 0

    Compatibilidade:
        - Se tol_inf e tol_sup não forem informados:
            usa tolerancia como:
                tol_inf = tolerancia
                tol_sup = tolerancia
    """

    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    c = np.asarray(c, dtype=float)

    # =========================
    # Validações básicas
    # =========================

    if A.size == 0 or b.size == 0 or c.size == 0:
        raise ValueError("Parâmetros inválidos para programação linear")

    if A.shape[0] != b.shape[0]:
        raise ValueError("Dimensão inconsistente: linhas de A devem igualar tamanho de b")

    if A.shape[1] != c.shape[0]:
        raise ValueError("Dimensão inconsistente: colunas de A devem igualar tamanho de c")

    if np.any(b < 0):
        raise ValueError("O vetor b não pode conter valores negativos")

    # =========================
    # Definição das tolerâncias
    # =========================

    if tol_inf is None and tol_sup is None:
        if tolerancia is None:
            tolerancia = 0.05

        if not (0 <= tolerancia < 1):
            raise ValueError("tolerancia deve estar entre 0 e 1")

        tol_inf = 0
        tol_sup = tolerancia

    else:
        # modo novo (assimétrico)
        tol_inf = 0.0 if tol_inf is None else tol_inf
        tol_sup = 0.0 if tol_sup is None else tol_sup

        if not (0 <= tol_inf < 1):
            raise ValueError("tol_inf deve estar entre 0 e 1")

        if tol_sup < 0:
            raise ValueError("tol_sup deve ser >= 0")

    # =========================
    # Construção das restrições
    # =========================

    b_upper = b * (1 + tol_sup)

    A_ub = A
    b_ub = b_upper

    # Comportamento especial
    if tol_inf == 0:
        # Ax >= b  →  -Ax <= -b
        A_lb = -A
        b_lb = -b

    else:
        # intervalo completo
        b_lower = b * (1 - tol_inf)
        A_lb = -A
        b_lb = -b_lower

    A_final = np.vstack([A_lb, A_ub])
    b_final = np.concatenate([b_lb, b_ub])

    # =========================
    # Solver
    # =========================

    result = linprog(
        c,
        A_ub=A_final,
        b_ub=b_final,
        bounds=[(0, None)] * len(c),
        method="highs"
    )

    # =========================
    # Tratamento
    # =========================

    if not result.success:
        raise ValueError(f"Falha no solver: {result.message}")

    x = result.x

    if x is None or np.allclose(x, 0):
        raise ValueError("Solução inválida ou trivial encontrada")

    return x