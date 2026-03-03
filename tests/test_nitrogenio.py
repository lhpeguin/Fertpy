import pytest
from fertpy import Nitrogenio


# =========
# Fixtures
# =========

@pytest.fixture
def nitrogenio_graos():
    return Nitrogenio("milho", "graos")


@pytest.fixture
def nitrogenio_silagem():
    return Nitrogenio("milho", "silagem")


# ========================
# GRÃOS – Matriz completa
# ========================

@pytest.mark.parametrize(
    "produtividade, classe_n, esperado",
    [
        # <6
        (5, "media_baixa", 60),
        (5, "alto", 90),

        # 6–8
        (7, "media_baixa", 90),
        (7, "alto", 120),

        # 8–10
        (9, "media_baixa", 120),
        (9, "alto", 160),

        # 10–12
        (11, "media_baixa", 140),
        (11, "alto", 200),

        # >12
        (13, "media_baixa", 160),
        (13, "alto", 220),
    ]
)
def test_nitrogenio_graos_matriz(
    nitrogenio_graos, produtividade, classe_n, esperado
):
    resultado = nitrogenio_graos.calcular(classe_n, produtividade)
    assert resultado.dose == esperado


# ==========================
# SILAGEM – Matriz completa
# ==========================

@pytest.mark.parametrize(
    "produtividade, classe_n, esperado",
    [
        # <45
        (44, "media_baixa", 60),
        (44, "alto", 90),

        # 45–55
        (50, "media_baixa", 90),
        (50, "alto", 120),

        # 55–60
        (58, "media_baixa", 120),
        (58, "alto", 160),

        # 60–65
        (63, "media_baixa", 140),
        (63, "alto", 200),

        # >65
        (70, "media_baixa", 160),
        (70, "alto", 220),
    ]
)
def test_nitrogenio_silagem_matriz(
    nitrogenio_silagem, produtividade, classe_n, esperado
):
    resultado = nitrogenio_silagem.calcular(classe_n, produtividade)
    assert resultado.dose == esperado
