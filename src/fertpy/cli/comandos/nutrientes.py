from fertpy.formulacao.fornecimento import NutrientesFornecidos


def comando_nutrientes(args):

    servico = NutrientesFornecidos(boletim=args.boletim)

    resultado, fert = servico.calcular(
        entrada_fonte=args.fonte,
        dose=args.dose
    )

    print(f"\nFonte: {fert.nome}")
    print(f"Dose aplicada: {args.dose:.2f} kg/ha")

    print("\nNutrientes fornecidos:\n")

    for nutriente, quantidade in resultado.items():
        print(f"{nutriente}: {quantidade:.2f} kg")