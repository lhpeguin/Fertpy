import pytest
from fertpy import Calagem


@pytest.fixture
def calagem():
    return Calagem("milho")


def test_calagem_formula_basica(calagem):
    resultado = calagem.calcular(v_atual=50, ctc=10)
    assert resultado == 0.5


def test_calagem_limite_maximo(calagem):
    resultado = calagem.calcular(v_atual=10, ctc=20)
    assert resultado == 1.5


def test_calagem_limite_minimo(calagem):
    resultado = calagem.calcular(v_atual=68, ctc=5)
    assert resultado == 0.5


def test_calagem_sem_necessidade(calagem):
    resultado = calagem.calcular(v_atual=75, ctc=10)
    assert resultado == 0
