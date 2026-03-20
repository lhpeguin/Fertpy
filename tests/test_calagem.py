import yaml
from importlib import resources

from fertpy import Calagem


def carregar_yaml():

    with resources.files("tests.knowledge") \
        .joinpath("calagem.yaml") \
        .open("r", encoding="utf-8") as f:

        return yaml.safe_load(f)


def test_calagem():

    data = carregar_yaml()["casos"]
    calagem = Calagem("milho")

    for caso in data:

        resultado = calagem.calcular(**caso["entrada"])

    assert resultado["dose"] == caso["esperado"]

