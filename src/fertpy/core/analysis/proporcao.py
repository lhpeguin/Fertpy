from math import gcd
from functools import reduce
from fractions import Fraction

# Ordem padrão agronômica
ORDEM_PADRAO = ["N", "P2O5", "K2O"]


# =========================
# Utilidades internas
# =========================

def _mdc_lista(valores: list[int]) -> int:
    valores = [v for v in valores if v != 0]

    if not valores:
        return 1  # evita divisão por zero

    return reduce(gcd, valores)

def _filtrar_positivos(valores: dict[str, float]) -> dict[str, float]:
    return {k: v for k, v in valores.items() if v > 0}


def _ordenar(valores: dict[str, float]) -> dict[str, float]:
    return {k: valores[k] for k in ORDEM_PADRAO if k in valores}


def _escalar_para_inteiros(valores: list[float], escala: int = 100) -> list[int]:
    return [int(round(v * escala)) for v in valores]


# =========================
# Núcleo de cálculo
# =========================

def normalizar_proporcao(valores: dict[str, float]) -> dict[str, float]:
    valores = _ordenar(valores)

    # pega apenas positivos para calcular o mínimo
    positivos = [v for v in valores.values() if v > 0]

    if not positivos:
        # tudo zero
        return {k: 0 for k in valores}

    minimo = min(positivos)

    # normaliza mantendo zeros
    return {
        k: (v / minimo if v > 0 else 0)
        for k, v in valores.items()
    }

def simplificar_proporcao(proporcao: dict[str, float]) -> dict[str, int]:
    if not proporcao:
        return {}

    proporcao = _ordenar(proporcao)

    # Converte para frações exatas
    fracoes = [Fraction(v).limit_denominator() for v in proporcao.values()]

    # MMC dos denominadores
    denominadores = [f.denominator for f in fracoes]
    mmc = reduce(lambda a, b: a * b // gcd(a, b), denominadores)

    # Converte tudo para inteiros equivalentes
    inteiros = [int(f * mmc) for f in fracoes]

    # Simplifica pelo MDC
    divisor = _mdc_lista(inteiros)
    simplificados = [v // divisor for v in inteiros]

    return dict(zip(proporcao.keys(), simplificados))


# =========================
# API de domínio
# =========================

def calcular_proporcao_demanda(demanda: dict[str, float]) -> dict[str, float]:
    return normalizar_proporcao(demanda)


def calcular_proporcao_fonte(nutrientes: dict[str, float]) -> dict[str, float]:
    return normalizar_proporcao(nutrientes)


def proporcao_inteira_demanda(demanda: dict[str, float]) -> dict[str, int]:
    return simplificar_proporcao(normalizar_proporcao(demanda))


def proporcao_inteira_fonte(nutrientes: dict[str, float]) -> dict[str, int]:
    return simplificar_proporcao(normalizar_proporcao(nutrientes))


# =========================
# Formatação
# =========================

def formatar_proporcao(
    proporcao: dict[str, float],
    incluir_labels: bool = False,
    forcar_inteiro: bool = False
) -> str:
    if not proporcao:
        return ""

    proporcao = _ordenar(proporcao)

    if forcar_inteiro:
        proporcao = simplificar_proporcao(proporcao)

    partes = []

    for v in proporcao.values():
        if isinstance(v, int) or abs(v - round(v)) < 1e-6:
            partes.append(str(int(round(v))))
        else:
            partes.append(f"{v:.2f}".rstrip("0").rstrip("."))

    resultado = ":".join(partes)

    if incluir_labels:
        labels = ":".join(proporcao.keys())
        return f"{labels} = {resultado}"

    return resultado
