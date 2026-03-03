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

from importlib import resources
from typing import Dict


caminho = "fertpy.knowledge"


def extrair_parametros() -> Dict[str, Dict[str, list[str]]]:
    estrutura = {}
    base = resources.files(caminho)

    for boletim in base.iterdir():
        if not boletim.is_dir() or boletim.name.startswith("_"):
            continue

        cultura_dict = {}
        
        pasta_adubacao = boletim / "adubacao"
        if not pasta_adubacao.exists():
            continue

        for cultura in pasta_adubacao.iterdir():
            if not cultura.is_dir() or cultura.name.startswith("_"):
                continue
                
            finalidades = [
                finalidade.name
                for finalidade in cultura.iterdir()
                if finalidade.is_dir and not finalidade.name.startswith("_")
            ]

            cultura_dict[cultura.name] = sorted(finalidades)

        estrutura[boletim.name] = cultura_dict

    return estrutura
