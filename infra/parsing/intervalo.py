import re

from fertpy.core.domain.intervalo import Intervalo


def parse_intervalo(texto: str) -> Intervalo:
    texto = texto.strip()

    #===============================================
    # Forma matematica: x <= a <= y, x < a < y, etc
    #===============================================

    padrao_duplo = re.compile(
        r"^\s*(-?\d+\.?\d*)\s*(<=|<)\s*[a-zA-Z_]+\s*(<=|<)\s*(-?\d+\.?\d*)\s*$"
    )

    m = padrao_duplo.match(texto)

    if m:
        a = float(m.group(1))
        limite_inferior = m.group(2)
        limite_superior = m.group(3)
        b = float(m.group(4))

        if a >= b:
            raise ValueError(f"intervalo inválido (a >= b): {texto}")

        inc_min = limite_inferior == "<="
        inc_max = limite_superior == "<="

        return Intervalo(a, b, inc_min, inc_max)
    
    #============================
    # Intervalos abertos simples
    #============================

    if texto.startswith(">="):
        return Intervalo(float(texto[2:].strip()), None, True, False)
    
    if texto.startswith("<="):
        return Intervalo(None, float(texto[2:].strip()), False, True)
    
    if texto.startswith(">"):
        return Intervalo(float(texto[1:].strip()), None, False, False)
    
    if texto.startswith("<"):
        return Intervalo(None, float(texto[1:].strip()), False, False)
    
    #=============
    # Valor exato
    #=============

    try:
        v = float(texto)
        return Intervalo(v, v, True, True)
    except ValueError:
        pass

    raise ValueError(f"Intervalo inválido: {texto}")
