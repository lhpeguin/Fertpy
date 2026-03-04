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

from fertpy.infra.loaders.correcao_loader import carregar_modelo_correcao
from fertpy.core.engine.calculo_calagem import CalagemEngine


class Calagem:

    def __init__(self, cultura: str):

        yaml = carregar_modelo_correcao(
            "boletim_100",
            cultura
        )["calagem"]

        self.modelo = yaml

    def calcular(
        self,
        v_atual: float,
        ctc: float,
        prnt: float | None = None
    ) -> float:

        parametros = self.modelo["parametros"]
        limites = self.modelo.get("limites", {})

        return CalagemEngine.calcular(
            v1=v_atual,
            ctc=ctc,
            v2=parametros["v2_desejado"],
            prnt=prnt or parametros["prnt_padrao"],
            dose_maxima=limites.get("dose_maxima"),
            dose_minima=limites.get("dose_minima")
        )
