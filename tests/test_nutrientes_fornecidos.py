import yaml
from importlib import resources

from fertpy.core.engine.nutriente_fornecido import nutrientes_fornecidos
from fertpy.core.factories.criador_fertilizante import criar_fertilizante
from fertpy.infra.loaders.fonte_loader import carregar_fontes
from fertpy.infra.parsing.fontes import resolver_fontes


def carregar_casos():

    with resources.files("tests.knowledge") \
        .joinpath("nutrientes_fornecidos.yaml") \
        .open("r", encoding="utf-8") as f:

        return yaml.safe_load(f)


def criar_fonte_yaml(nome, tipo="adubacao", boletim="boletim_100"):
    fontes_yaml = carregar_fontes(boletim, tipo=tipo)

    resolvidas = resolver_fontes([nome], fontes_yaml)

    return criar_fertilizante(*resolvidas[0])


def test_nutrientes_fornecidos():

    casos = carregar_casos()

    for caso in casos:

        fert = criar_fonte_yaml(caso["fonte"])

        resultado = nutrientes_fornecidos(
            dose=caso["dose"],
            fertilizer=fert
        )

        esperado = caso["esperado"]

        for nutriente, valor_esperado in esperado.items():

            assert nutriente in resultado, (
                f"Nutriente '{nutriente}' não encontrado no resultado "
                f"para fonte '{caso['fonte']}'"
            )

            valor_obtido = resultado[nutriente]

            assert abs(valor_obtido - valor_esperado) < 0.01, (
                f"Erro no cálculo de {nutriente} para '{caso['fonte']}': "
                f"esperado {valor_esperado}, obtido {valor_obtido}"
            )
