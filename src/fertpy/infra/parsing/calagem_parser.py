from fertpy.core.domain.calagem_model import (
    ModeloCalagem,
    ParametrosCalagem,
    RecomendacoesCalagem
)


def parse_calagem_model(data: dict) -> ModeloCalagem:

    # ========================
    # Parâmetros
    # ========================
    params = data.get("parametros")
    if not params:
        raise ValueError("Parâmetros de calagem não encontrados")

    parametros = ParametrosCalagem(
        v2_desejado=params.get("v2_desejado"),
        prnt_padrao=params.get("prnt_padrao")
    )

    if parametros.v2_desejado is None:
        raise ValueError("v2_desejado é obrigatório")

    # ========================
    # Recomendações
    # ========================
    rec = data.get("recomendacoes")

    recomendacoes = None
    if rec:
        recomendacoes = RecomendacoesCalagem(
            parcelamento_acima_de=rec.get("parcelamento_acima_de"),
            mensagem_parcelamento=rec.get("mensagem_parcelamento")
        )

    # ========================
    # Modelo final
    # ========================
    return ModeloCalagem(
        parametros=parametros,
        recomendacoes=recomendacoes,
        unidade_saida=data.get("unidade_saida")
    )
