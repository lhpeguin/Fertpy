def positivo(value):
    v = float(value)
    if v <= 0:
        raise ValueError("A dose deve ser maior que zero")
    return v


def configurar_nutrientes(parser):

    parser.add_argument(
        "--fonte",
        type=str,
        required=True,
        help=(
            "Fonte de fertilizante.\n"
            "Pode ser:\n"
            "  • Nome do YAML: ureia, map, kcl\n"
            "  • Fonte custom: meu_adubo:N=10,P2O5=20,K2O=10"
        )
    )

    parser.add_argument(
        "--dose",
        type=positivo,
        required=True,
        help="Dose aplicada (kg/ha)"
    )

    parser.add_argument(
        "--boletim",
        type=str,
        default="boletim_100",
        help="Base de conhecimento utilizada (ex: boletim_100)"
    )

    parser.add_argument(
        "--tipo",
        choices=["adubacao", "calagem"],
        default="adubacao",
        help="Tipo de fonte utilizada"
    )
