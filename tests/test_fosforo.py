import pytest
from fertpy import Fosforo


# =========
# Fixtures
# =========

@pytest.fixture
def fosforo_graos():
    return Fosforo("milho", "graos")


@pytest.fixture
def fosforo_silagem():
    return Fosforo("milho", "silagem")


# ========================
# GRÃOS – Matriz Numérica
# ========================

@pytest.mark.parametrize(
    "p_resina, produtividade, esperado",
    [
        # <6
        (10, 5.5, 90),
        (25, 5.5, 60),
        (50, 5.5, 30),

        # 6–8
        (10, 7, 100),
        (25, 7, 70),
        (50, 7, 40),

        # 8–10
        (10, 9, 120),
        (25, 9, 90),
        (50, 9, 60),

        # 10–12
        (25, 11, 110),
        (50, 11, 70),

        # >12
        (25, 13, 120),
        (50, 13, 80),
    ]
)
def test_fosforo_graos_matriz(fosforo_graos, p_resina, produtividade, esperado):
    resultado = fosforo_graos.calcular(p_resina, produtividade)
    assert resultado.dose == esperado


# ========================
# GRÃOS – Bordas críticas
# ========================

@pytest.mark.parametrize(
    "p_resina, esperado",
    [
        (15.9, 100),
        (16, 70),
        (40, 70),
        (40.1, 40),
    ]
)
def test_fosforo_graos_bordas(fosforo_graos, p_resina, esperado):
    resultado = fosforo_graos.calcular(p_resina, 6)
    assert resultado.dose == esperado


# =========================
# GRÃOS – Regras especiais
# =========================

def test_fosforo_graos_arranque(fosforo_graos):
    resultado = fosforo_graos.calcular(85, 8)

    assert isinstance(resultado.dose, dict)
    assert resultado.dose["min"] == 20
    assert resultado.dose["max"] == 40


def test_fosforo_graos_bloqueio(fosforo_graos):
    resultado = fosforo_graos.calcular(10, 11)
    assert resultado.dose is None


# ==========================
# SILAGEM – Matriz Numérica
# ==========================

@pytest.mark.parametrize(
    "p_resina, produtividade, esperado",
    [
        # <45
        (10, 40, 90),
        (25, 40, 60),
        (50, 40, 30),

        # 45–55
        (10, 50, 100),
        (25, 50, 70),
        (50, 50, 40),

        # 55–60
        (10, 58, 120),
        (25, 58, 90),
        (50, 58, 60),

        # 60–65
        (25, 63, 110),
        (50, 63, 70),

        # >65
        (25, 70, 120),
        (50, 70, 80),
    ]
)
def test_fosforo_silagem_matriz(fosforo_silagem, p_resina, produtividade, esperado):
    resultado = fosforo_silagem.calcular(p_resina, produtividade)
    assert resultado.dose == esperado
