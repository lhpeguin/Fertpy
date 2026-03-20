import argparse

from fertpy.cli.comandos.formular import comando_formular
from fertpy.cli.comandos.nutrientes import comando_nutrientes
from fertpy.cli.argumentos.formular_args import configurar_formular
from fertpy.cli.argumentos.nutrientes_args import configurar_nutrientes


def main():

    parser = argparse.ArgumentParser(
        description="Fertpy CLI - Ferramentas para cálculo de adubação e nutrientes"
    )

    subparsers = parser.add_subparsers(dest="comando")

    # =================
    # Formular
    # =================
    parser_formular = subparsers.add_parser(
        "formular",
        help="Calcula formulação de fertilizantes"
    )

    configurar_formular(parser_formular)
    parser_formular.set_defaults(func=comando_formular)

    # =================
    # Nutrientes
    # =================
    parser_nutrientes = subparsers.add_parser(
        "nutrientes",
        help="Calcula nutrientes fornecidos por uma dose"
    )

    configurar_nutrientes(parser_nutrientes)
    parser_nutrientes.set_defaults(func=comando_nutrientes)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()