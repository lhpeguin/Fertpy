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

@dataclass(frozen=True)
class Intervalo:
    minimo: float | None
    maximo: float | None
    inclui_min: bool = True
    inclui_max: bool = False

    def __post_init__(self):
        if self.minimo is not None and self.maximo is not None:
            if self.minimo > self.maximo:
                raise ValueError("Minimo não pode ser maior que o maximo")
        
    def contem(self, valor:float) -> bool:
        if self.minimo is not None:
            if self.inclui_min and valor < self.minimo:
                return False
            if not self.inclui_min and valor <= self.minimo:    
                return False
        
        if self.maximo is not None:
            if self.inclui_max and valor > self.maximo:
                return False
            if not self.inclui_max and valor >= self.maximo:
                return False
        
        return True
