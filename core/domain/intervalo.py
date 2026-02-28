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
