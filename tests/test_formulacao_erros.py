import pytest

from fertpy.core.engine.formulacao_adubacao import formular
from fertpy.core.factories.criador_fertilizante import criar_fertilizante
from fertpy.infra.loaders.fonte_loader import carregar_fontes
from fertpy.infra.parsing.fontes import resolver_fontes


def criar_fonte_yaml(nome, tipo="adubacao", boletim="boletim_100"):
    fontes_yaml = carregar_fontes(boletim, tipo=tipo)

    resolvidas = resolver_fontes([nome], fontes_yaml)

    return criar_fertilizante(*resolvidas[0])


def test_sem_fonte_para_nutriente():

    ureia = criar_fonte_yaml("ureia")

    demanda = {
        "K2O": 60
    }

    with pytest.raises(ValueError):
        formular(demanda, [ureia])
