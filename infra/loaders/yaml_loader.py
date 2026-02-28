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
import yaml

def carregar_modelo(boletim: str, cultura: str, nutriente:str):
    pacote_base = f"fertpy.knowledge.{boletim}.{cultura}"
    nome_arquivo = f"{nutriente}.yaml"

    with resources.files(pacote_base).joinpath(nome_arquivo).open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
