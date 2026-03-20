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

from dataclasses import dataclass, replace

from fertpy.infra.loaders.adubacao_loader import carregar_modelo_adubacao
from fertpy.infra.parsing.modelo_agronomico import parse_modelo_agronomico
from fertpy.core.engine.avaliador import Avaliador
from fertpy.services.validacao_parametros import validar_parametros
from fertpy.core.engine.fracionamento.nitrogenio import separar_nitrogenio

@dataclass
class Nitrogenio:

    def __init__(self, cultura: str, finalidade: str):

        boletim, cultura, finalidade = validar_parametros(
            "boletim_100",
            cultura,
            finalidade
        )
        
        yaml = carregar_modelo_adubacao(
            boletim,
            cultura,
            finalidade, 
            "nitrogenio"
        )["nitrogenio"]
        
        parseado = parse_modelo_agronomico(yaml)
        self.modelo = parseado

    def calcular(
        self,
        classe_resp_n: str,
        produtividade: float
    ):

        contexto = {
            "classe_resp_N": classe_resp_n,
            "produtividade": produtividade
        }

        resultado = Avaliador.avaliar(
            criterios=self.modelo.criterios,
            contexto=contexto,
            nutriente=self.modelo.nutriente,
            nutriente_recomendado=self.modelo.nutriente_recomendado,
            unidade=self.modelo.unidade_saida,
            observacoes=None,
            fonte=self.modelo.fonte_referencia
        )

        if self.modelo.fracionamento:
            fracionado = separar_nitrogenio(
                total_n=resultado.dose,
                regra=self.modelo.fracionamento
            )

            return replace(resultado, fracionamento=fracionado)

        return resultado
