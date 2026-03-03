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
from typing import Any

from fertpy.core.domain.intervalo import Intervalo
from fertpy.core.domain.classe import Classe


@dataclass(frozen=True)
class Criterio:

    condicoes: dict[str, Intervalo | str]
    classe: Classe | None
    recomendacao: Any

    observacoes: str | None = None

    def __post_init__(self):

        if not isinstance(self.condicoes, dict):
            raise TypeError("Condições deve ser um dict")

        if not self.condicoes:
            raise ValueError("Criterio precisa de pelo menos uma condição")

        for nome, condicao in self.condicoes.items():

            if not isinstance(nome, str) or not nome.strip():
                # ==================================
                # inserir função parametros validos
                # ==================================
                raise TypeError("Nome de condição inválido")

            if not isinstance(condicao, (Intervalo, str)):
                raise TypeError(f"Condição inválida para {nome}")

        if self.classe is not None and not isinstance(self.classe, Classe):
            raise TypeError("Classe deve ser Classe ou None")
