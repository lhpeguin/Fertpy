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

from fertpy.utils.parametros import extrair_parametros


def imprimir_parametros(estrutura: dict[str, dict[str, list[str]]]) -> None:
    linhas = []

    for boletim, culturas in estrutura.items():
        linhas.append(f"\nboletim: {boletim}")

        for cultura, nutrientes in culturas.items():
            linhas.append(f"  Cultura: {cultura}")
        
            for nutriente in nutrientes:
                linhas.append(f"    - {nutriente}")

    return "\n".join(linhas)

def imprimir_parametros_cli():
    dados = extrair_parametros()
    print(imprimir_parametros(dados))
