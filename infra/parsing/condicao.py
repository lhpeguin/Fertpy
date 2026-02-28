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

from fertpy.infra.parsing.intervalo import parse_intervalo


def parse_condicao(valor):
    if isinstance(valor, (int, float)):
        return parse_intervalo(str(valor))
    
    if isinstance(valor, str):
        try:
            return parse_intervalo(valor)
        except ValueError:
            return valor.strip()
    
    return valor