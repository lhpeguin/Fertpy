import yaml
from importlib import resources

from fertpy import Nitrogenio


def carregar_yaml():

    with resources.files("tests.knowledge") \
        .joinpath("nitrogenio.yaml") \
        .open("r", encoding="utf-8") as f:

        return yaml.safe_load(f)


def test_nitrogenio_graos():

    data = carregar_yaml()["graos"]
    nitrogenio = Nitrogenio("milho", "graos")

    for caso in data["matriz"]:

        resultado = nitrogenio.calcular(
            caso["classe_n"],
            caso["produtividade"]
        )

        assert resultado.dose == caso["esperado"]


def test_nitrogenio_silagem():

    data = carregar_yaml()["silagem"]
    nitrogenio = Nitrogenio("milho", "silagem")

    for caso in data["matriz"]:

        resultado = nitrogenio.calcular(
            caso["classe_n"],
            caso["produtividade"]
        )

        assert resultado.dose == caso["esperado"]
