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

from fertpy.core.domain.criterio import Criterio


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
