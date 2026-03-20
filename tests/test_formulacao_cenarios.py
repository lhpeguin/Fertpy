import yaml
import pytest
from importlib import resources

from fertpy.formulacao.adubacao import FormulacaoAdubacao
from fertpy.formulacao.calagem import FormulacaoCalagem


# =========================
# Carregar cenários
# =========================
def carregar_cenarios():

    arquivos = [
        "formulacao_cenarios_adubacao.yaml",
        "formulacao_cenarios_calagem.yaml"
    ]

    cenarios = []
    base = resources.files("tests.knowledge")

    for arquivo in arquivos:
        with base.joinpath(arquivo).open("r", encoding="utf-8") as f:
            dados = yaml.safe_load(f)

            if dados:
                cenarios.extend(dados)

    return cenarios


# =========================
# Serviço
# =========================
def obter_servico(tipo: str):
    if tipo == "adubacao":
        return FormulacaoAdubacao()
    elif tipo == "calagem":
        return FormulacaoCalagem()
    else:
        raise ValueError(f"Tipo desconhecido: {tipo}")


# =========================
# Montar fontes
# =========================
def montar_entradas_fontes(caso: dict) -> list[str]:
    entradas = []

    entradas.extend(caso.get("fontes_yaml", []))

    for fonte in caso.get("fontes_custom", []):
        garantias_str = ",".join(
            f"{k}={v}" for k, v in fonte["garantias"].items()
        )
        entradas.append(f"{fonte['nome']}:{garantias_str}")

    return entradas


# =========================
# Normalização de nomes
# =========================
MAPA_FONTES = {
    "ureia": "ureia",
    "map": "map",
    "cloreto de potássio": "kcl",
    "calcário agrícola": "calcario_agricola",
}


def normalizar_nome(nome: str) -> str:
    chave = nome.strip().lower()
    return MAPA_FONTES.get(chave, chave)


# =========================
# Teste principal
# =========================
def test_formulacao_cenarios():

    cenarios = carregar_cenarios()

    for caso in cenarios:

        tipo = caso.get("tipo", "adubacao")
        servico = obter_servico(tipo)

        entradas_fontes = montar_entradas_fontes(caso)
        esperado = caso["esperado"]

        # =========================
        # Caso de erro
        # =========================
        if esperado == "erro":

            with pytest.raises(ValueError):
                if tipo == "adubacao":
                    servico.calcular(
                        demanda=caso["demanda"],
                        entradas_fontes=entradas_fontes
                    )
                else:
                    servico.calcular(
                        cultura=caso["cultura"],
                        v_atual=caso["v_atual"],
                        ctc=caso["ctc"],
                        entradas_fontes=entradas_fontes
                    )
            continue

        # =========================
        # Execução
        # =========================
        if tipo == "adubacao":
            resultado = servico.calcular(
                demanda=caso["demanda"],
                entradas_fontes=entradas_fontes,
                precos=caso.get("precos"),
                fretes=caso.get("fretes"),
                tolerancia=caso.get("tolerancia", 0.05),
                modo=caso.get("modo", "mistura")
            )
            
        else:
            resultado = servico.calcular(
                cultura=caso["cultura"],
                v_atual=caso["v_atual"],
                ctc=caso["ctc"],
                entradas_fontes=entradas_fontes,
                precos=caso.get("precos"),
                fretes=caso.get("fretes"),
                tolerancia=caso.get("tolerancia", 0.05)
            )

        doses = resultado["doses"]

        # =========================
        # Validação
        # =========================
        for fonte_yaml, dose_esperada in esperado.items():

            fonte_id = normalizar_nome(fonte_yaml)

            assert fonte_id in doses, (
                f"{fonte_yaml} ({fonte_id}) não encontrada no resultado {doses}"
            )

            assert pytest.approx(
                doses[fonte_id],
                rel=1e-2
            ) == dose_esperada, (
                f"Erro na dose de {fonte_yaml}: "
                f"esperado {dose_esperada}, obtido {doses[fonte_id]}"
            )
