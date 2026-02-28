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

class CalagemEngine:

    @staticmethod
    def calcular(
        v1: float,
        ctc: float,
        v2: float,
        prnt: float,
        dose_maxima: float | None = None,
        dose_minima: float | None = None
    ) -> float:

        nc = (ctc * (v2 - v1)) / (10 * prnt)

        if nc <= 0:
            return 0.0

        if dose_maxima is not None and nc > dose_maxima:
            nc = dose_maxima

        if dose_minima is not None and nc < dose_minima:
            return 0.0

        return round(nc, 2)