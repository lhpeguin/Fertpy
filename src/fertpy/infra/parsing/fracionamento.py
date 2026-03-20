def plantio_safe_number(valor):
    if not isinstance(valor, (int, float)):
        raise TypeError("Valores de fracionamento devem ser numéricos")
    return float(valor)

def parse_fracionamento(dados):
    if not dados:
        return None

    if not isinstance(dados, dict):
        raise TypeError("fracionamento deve ser um dict")

    estrategia = dados.get("estrategia")

    if not estrategia:
        raise ValueError("fracionamento deve conter 'estrategia'")

    if estrategia == "threshold":

        if "threshold" not in dados:
            raise ValueError("estrategia 'threshold' requer 'threshold'")

        if "plantio" not in dados:
            raise ValueError("fracionamento deve conter 'plantio'")

        plantio = dados["plantio"]

        if "min" not in plantio or "max" not in plantio:
            raise ValueError("plantio deve conter 'min' e 'max'")

        return {
            "estrategia": "threshold",
            "threshold": plantio_safe_number(dados["threshold"]),
            "plantio": {
                "min": plantio_safe_number(plantio["min"]),
                "max": plantio_safe_number(plantio["max"]),
            }
        }

    raise ValueError(f"Estrategia de fracionamento desconhecida: {estrategia}")
