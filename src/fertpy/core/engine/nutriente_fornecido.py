def nutrientes_fornecidos(dose, fertilizer):

    resultado = {}

    for nutriente, teor in fertilizer.nutrientes.items():

        resultado[nutriente] = dose * teor / 100

    return resultado
