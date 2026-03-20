from fertpy.formulacao.adubacao import FormulacaoAdubacao
from fertpy.formulacao.calagem import FormulacaoCalagem


# ========================
# Parser de preços
# ========================
def parse_precos(lista):
    if not lista:
        return None

    precos = {}

    for item in lista:
        try:
            nome, valor = item.split("=")
            precos[nome.strip().lower()] = float(valor)
        except ValueError:
            raise ValueError(
                f"Formato inválido: '{item}'. Use fonte=valor (ex: ureia=200)"
            )

    return precos


def comando_formular(args):

    # ========================
    # Parse de preços
    # ========================
    precos = parse_precos(getattr(args, "precos", None))
    fretes = parse_precos(getattr(args, "fretes", None))

    # ========================
    # Execução
    # ========================
    if args.tipo == "adubacao":

        formulador = FormulacaoAdubacao()

        demanda = {}

        if args.n and args.n > 0:
            demanda["N"] = args.n
        if args.p and args.p > 0:
            demanda["P2O5"] = args.p
        if args.k and args.k > 0:
            demanda["K2O"] = args.k

        resultado = formulador.calcular(
            demanda=demanda,
            entradas_fontes=args.fontes,
            precos=precos,
            fretes=fretes,
            solver=args.solver,
            tolerancia=args.tolerancia,
            modo=args.modo
        )

    elif args.tipo == "calagem":

        formulador = FormulacaoCalagem()

        resultado = formulador.calcular(
            cultura=args.cultura,
            v_atual=args.v_atual,
            ctc=args.ctc,
            entradas_fontes=args.fontes,
            precos=precos,
            fretes=fretes,
            solver=args.solver,
            tolerancia=args.tolerancia
        )

    else:
        print("Tipo inválido. Use 'adubacao' ou 'calagem'.")
        return

    # ========================
    # Output
    # ========================
    doses = resultado.get("doses", {})
    unidade = resultado.get("unidade", "")

    if not doses:
        print("Nenhuma dose necessária.")
        return

    print("\n=== Resultado da formulação ===")

    custo_por_fonte = resultado.get("custo_por_fonte") or {}

    for fonte, dose in doses.items():
        linha = f"{fonte}: {dose:.2f} {unidade}"

        custo_fonte = custo_por_fonte.get(fonte)
        if custo_fonte is not None:
            linha += f" (R$ {custo_fonte:.2f}/ha)"

        print(linha)

    # ========================
    # Custo total
    # ========================
    custo_total = resultado.get("custo_total")

    if custo_total is not None:
        print("\n----------------------")
        print(f"Custo total: R$ {custo_total:.2f}/ha")
