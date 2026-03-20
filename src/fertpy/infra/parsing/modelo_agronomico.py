# Copyright 2026 Luiz Henrique de Lima Peguin
# and Pedro Henrique Escaranaro Brasil
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

from fertpy.infra.parsing.condicao import parse_condicao
from fertpy.core.domain.classe import Classe
from fertpy.core.domain.criterio import Criterio
from fertpy.core.domain.modelo_agronomico import ModeloAgronomico
from fertpy.infra.parsing.fracionamento import parse_fracionamento


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
    
    fracionamento = parse_fracionamento(
        modelo.get("fracionamento")
    )
    
    return ModeloAgronomico(
        nutriente=modelo["nutriente"],
        unidade_saida=modelo["unidade_saida"],
        criterios=criterios,
        nutriente_recomendado=modelo.get("nutriente_recomendado"),
        unidade_entrada=modelo.get("unidade_entrada"),
        metodo_analitico=modelo.get("metodo_analitico"),
        fonte_referencia=modelo.get("fonte_referencia"),
        fracionamento=fracionamento
    )