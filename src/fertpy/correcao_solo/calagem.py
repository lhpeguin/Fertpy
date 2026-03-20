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
from fertpy.infra.parsing.calagem_parser import parse_calagem_model
from fertpy.core.engine.calculo_calagem import CalagemEngine


class Calagem:

    def __init__(self, cultura: str):

        raw = carregar_modelo_correcao(
            "boletim_100",
            cultura
        )["calagem"]

        self.modelo = parse_calagem_model(raw)

    def calcular(
        self,
        v_atual: float,
        ctc: float,
        prnt: float | None = None
    ) -> dict:

        dose = CalagemEngine.calcular(
            v1=v_atual,
            ctc=ctc,
            v2=self.modelo.parametros.v2_desejado,
            prnt=prnt or self.modelo.parametros.prnt_padrao
        )

        observacoes = []

        rec = self.modelo.recomendacoes

        if rec and rec.parcelamento_acima_de:
            if dose > rec.parcelamento_acima_de:
                observacoes.append(rec.mensagem_parcelamento)

        return {
            "dose": dose,
            "observacoes": observacoes
        }
