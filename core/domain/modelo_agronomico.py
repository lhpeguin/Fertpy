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

from dataclasses import dataclass
from collections import defaultdict

from fertpy.core.domain.criterio import Criterio
from fertpy.core.domain.exceptions import ParametroInvalidoError


@dataclass(frozen=True)
class ModeloAgronomico:
    nutriente: str
    unidade_saida: str

    criterios: list[Criterio]

    nutriente_recomendado: str | None = None
    unidade_entrada: str | None = None
    metodo_analitico: str | None = None
    fonte_referencia: dict | None = None

    def __post_init__(self):

        if not self.nutriente:
            raise ValueError("O modelo não possui nutriente declarado")
        
        if not self.unidade_saida:
            raise ValueError("O modelo não possui unidade de saida declarado") 

        if not self.criterios:
            raise ValueError("Modelo precisa de critérios")

        for c in self.criterios:
            if not isinstance(c, Criterio):
                raise TypeError("Todos os critérios devem ser instâncias de criterio")

    @property
    def variaveis_esperadas(self) -> set[str]:
        variaveis = set()

        for criterio in self.criterios:
            variaveis.update(criterio.condicoes.keys())

        return variaveis
    
    def valores_discretos_por_variavel(self) -> dict[str, set]:

        valores = defaultdict(set)

        for criterio in self.criterios:
            for var, cond in criterio.condicoes.items():
                if isinstance(cond, str):
                    valores[var].add(cond)
        
        return valores
    
    def validar_contexto(self, contexto: dict):
        faltando = self.variaveis_esperadas - contexto.keys()
        if faltando:
            raise ValueError(
                f"Variáveis obrigatórias ausentes: {sorted(faltando)}"
            )
        
        extras = contexto.keys() - self.variaveis_esperadas
        if extras:
            raise ValueError(
                f"Variáveis inesperadas: {sorted(extras)}"
            )
        
        for var, valor in contexto.items():

            exemplos = [
                criterio.condicoes[var]
                for criterio in self.criterios
                if var in criterio.condicoes
            ]

            if not exemplos:
                continue

            exemplo = exemplos[0]

            if isinstance(exemplo, str):
                valores_validos = {
                    c.condicoes[var]
                    for c in self.criterios
                    if isinstance(c.condicoes[var], str)
                }

                if valor not in valores_validos:
                    raise ParametroInvalidoError(
                        var,
                        valor,
                        sorted(valores_validos)
                    )
            
            else:
                if not isinstance(valor, (int, float)):
                    raise TypeError(
                        f"Variável '{var}' deve ser numérica"
                    )
