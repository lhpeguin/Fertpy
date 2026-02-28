from fertpy.infra.parsing.condicao import parse_condicao
from fertpy.core.domain.classe import Classe
from fertpy.core.domain.criterio import Criterio
from fertpy.core.domain.modelo_agronomico import ModeloAgronomico


def parse_modelo_agronomico(modelo: dict) -> ModeloAgronomico:

    criterios = []

    for regra in modelo.get("regras", []):

        condicoes = {
            variavel: parse_condicao(expressao)
            for variavel, expressao in regra.get("condicoes", {}).items()
        }

        classe  = None
        if "classe" in regra:
            classe = Classe(nome=regra["classe"], descricao=None)
        
        recomendacao = regra.get("recomendacao")

        texto = regra.get("texto")
        if texto:
            texto = texto.strip()
        
        criterios.append(
            Criterio(
                condicoes=condicoes,
                classe=classe,
                recomendacao=recomendacao,
                observacoes=texto
            )
        )
    
    return ModeloAgronomico(
        nutriente=modelo["nutriente"],
        unidade_saida=modelo["unidade_saida"],
        criterios=criterios,
        nutriente_recomendado=modelo.get("nutriente_recomendado"),
        unidade_entrada=modelo.get("unidade_entrada"),
        metodo_analitico=modelo.get("metodo_analitico"),
        fonte_referencia=modelo.get("fonte_referencia")
    )