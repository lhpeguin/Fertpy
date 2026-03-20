import yaml
from importlib import resources

from fertpy import Fosforo


def carregar_yaml():

    with resources.files("tests.knowledge") \
        .joinpath("fosforo.yaml") \
        .open("r", encoding="utf-8") as f:

        return yaml.safe_load(f)


def test_fosforo_graos():

    data = carregar_yaml()["graos"]
    fosforo = Fosforo("milho", "graos")

    # MATRIZ
    for caso in data["matriz"]:

        resultado = fosforo.calcular(
            caso["p_resina"],
            caso["produtividade"]
        )

        assert resultado.dose == caso["esperado"]

    # BORDAS
    for caso in data["bordas"]:

        resultado = fosforo.calcular(
            caso["p_resina"],
            6  # produtividade fixa como no teste original
        )

        assert resultado.dose == caso["esperado"]

    # ESPECIAIS

    # Arranque
    caso = data["especiais"]["arranque"]

    resultado = fosforo.calcular(
        caso["entrada"]["p_resina"],
        caso["entrada"]["produtividade"]
    )

    assert isinstance(resultado.dose, dict)
    assert resultado.dose["min"] == caso["esperado"]["min"]
    assert resultado.dose["max"] == caso["esperado"]["max"]

    # Bloqueio
    caso = data["especiais"]["bloqueio"]

    resultado = fosforo.calcular(
        caso["entrada"]["p_resina"],
        caso["entrada"]["produtividade"]
    )

    assert resultado.dose is None


def test_fosforo_silagem():

    data = carregar_yaml()["silagem"]
    fosforo = Fosforo("milho", "silagem")

    for caso in data["matriz"]:

        resultado = fosforo.calcular(
            caso["p_resina"],
            caso["produtividade"]
        )

        assert resultado.dose == caso["esperado"]
