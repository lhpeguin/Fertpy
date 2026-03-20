import yaml
from importlib import resources

from fertpy import Potassio


def carregar_yaml():

    with resources.files("tests.knowledge") \
        .joinpath("potassio.yaml") \
        .open("r", encoding="utf-8") as f:

        return yaml.safe_load(f)


def test_potassio_graos():

    data = carregar_yaml()["graos"]
    potassio = Potassio("milho", "graos")

    # MATRIZ
    for caso in data["matriz"]:

        resultado = potassio.calcular(
            caso["k"],
            caso["produtividade"]
        )

        assert resultado.dose == caso["esperado"]

    # BORDAS
    for caso in data["bordas"]:

        resultado = potassio.calcular(
            caso["k"],
            6  # mesma lógica do teste original
        )

        assert resultado.dose == caso["esperado"]


def test_potassio_silagem():

    data = carregar_yaml()["silagem"]
    potassio = Potassio("milho", "silagem")

    for caso in data["matriz"]:

        resultado = potassio.calcular(
            caso["k"],
            caso["produtividade"]
        )

        assert resultado.dose == caso["esperado"]
