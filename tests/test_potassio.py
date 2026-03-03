import pytest
from fertpy import Potassio


# =========
# Fixtures
# =========

@pytest.fixture
def potassio_graos():
    return Potassio("milho", "graos")


@pytest.fixture
def potassio_silagem():
    return Potassio("milho", "silagem")


# ========================
# GRÃOS – Matriz completa
# ========================

@pytest.mark.parametrize(
    "k, produtividade, esperado",
    [
        # <6
        (1.2, 5.5, 70),
        (2.0, 5.5, 40),
        (3.2, 5.5, 30),

        # 6–8
        (1.2, 7, 90),
        (2.0, 7, 50),
        (3.2, 7, 30),

        # 8–10
        (1.2, 9, 100),
        (2.0, 9, 70),
        (3.2, 9, 40),

        # 10–12
        (1.2, 11, 110),
        (2.0, 11, 90),
        (3.2, 11, 50),

        # >12
        (1.2, 13, 120),
        (2.0, 13, 100),
        (3.2, 13, 60),
    ]
)
def test_potassio_graos_matriz(potassio_graos, k, produtividade, esperado):
    resultado = potassio_graos.calcular(k, produtividade)
    assert resultado.dose == esperado


# ========================
# GRÃOS – Bordas críticas
# ========================

@pytest.mark.parametrize(
    "k, esperado",
    [
        (1.59, 90),
        (1.6, 50),
        (3.0, 50),
        (3.01, 30),
    ]
)
def test_potassio_graos_bordas(potassio_graos, k, esperado):
    resultado = potassio_graos.calcular(k, 6)
    assert resultado.dose == esperado


# ==========================
# SILAGEM – Matriz completa
# ==========================

@pytest.mark.parametrize(
    "k, produtividade, esperado",
    [
        # <45
        (1.2, 40, 70),
        (2.0, 40, 40),
        (3.2, 40, 30),

        # 45–55
        (1.2, 50, 90),
        (2.0, 50, 50),
        (3.2, 50, 30),

        # 55–60
        (1.2, 58, 100),
        (2.0, 58, 70),
        (3.2, 58, 40),

        # 60–65
        (1.2, 63, 110),
        (2.0, 63, 90),
        (3.2, 63, 50),

        # >65
        (1.2, 70, 120),
        (2.0, 70, 100),
        (3.2, 70, 60),
    ]
)
def test_potassio_silagem_matriz(potassio_silagem, k, produtividade, esperado):
    resultado = potassio_silagem.calcular(k, produtividade)
    assert resultado.dose == esperado