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

from fertpy.core.domain.intervalo import Intervalo
from fertpy.core.domain.classe import Classe


@dataclass(frozen=True)
class Recomendacao:
    nutriente: str
    
    dose: float | Intervalo | str
    unidade: str

    classe: Classe

    nutriente_recomendado: str | None = None

    observacoes: list[str] | None = None
    fonte: dict | None = None
    fracionamento: dict | None = None

    def __post_init__(self):

        if not self.nutriente:
            raise ValueError("Recomendação precisa do parâmetro nutriente")
        
        if not self.unidade:
            raise ValueError("Recomendação precisa do parâmetro unidade")
