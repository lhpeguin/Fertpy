def separar_nitrogenio(total_n: float, regra: dict) -> dict:

    estrategia = regra["estrategia"]

    if estrategia == "threshold":
        threshold = regra["threshold"]
        n_min = regra["plantio"]["min"]
        n_max = regra["plantio"]["max"]

        if total_n <= threshold:
            n_plantio = n_min
        else:
            n_plantio = n_max

        n_cobertura = total_n - n_plantio

        return {
            "plantio": n_plantio,
            "cobertura": n_cobertura
        }

    raise ValueError(f"Estrategia desconhecida: {estrategia}")
