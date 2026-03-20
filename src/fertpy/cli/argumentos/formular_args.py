def configurar_formular(parser):

    # =========================
    # Tipo
    # =========================
    parser.add_argument(
        "--tipo",
        choices=["adubacao", "calagem"],
        required=True,
        help="Tipo de formulação"
    )

    # =========================
    # Adubação
    # =========================
    parser.add_argument("--n", type=float, help="Demanda de N")
    parser.add_argument("--p", type=float, help="Demanda de P2O5")
    parser.add_argument("--k", type=float, help="Demanda de K2O")

    # =========================
    # Calagem
    # =========================
    parser.add_argument("--cultura", type=str, help="Cultura (ex: milho)")

    parser.add_argument(
        "--v-atual",
        type=float,
        help="Saturação por bases atual (porcentagem)"
    )

    parser.add_argument(
        "--v-desejado",
        type=float,
        help="Saturação por bases desejada (porcentagem)"
    )

    parser.add_argument("--ctc", type=float, help="CTC")

    # =========================
    # Fontes
    # =========================
    parser.add_argument(
        "--fontes",
        nargs="+",
        required=True,
        help="Lista de fontes"
    )

    # =========================
    # Preços
    # =========================
    parser.add_argument(
        "--precos",
        nargs="+",
        help="Formato: fonte=valor"
    )

    # =========================
    # Fretes
    # =========================
    parser.add_argument(
        "--fretes",
        nargs="+",
        help="Formato: fonte=valor"
    )

    # =========================
    # Solver
    # =========================
    parser.add_argument(
        "--solver",
        default="quantidade_minima",
        choices=["quantidade_minima", "custo_minimo"],
        help="Tipo de solver"
    )

    # =========================
    # Tolerancia
    # =========================
    parser.add_argument(
        "--tolerancia",
        type=float,
        default=0.01,
        help="Tolerância aceitável para atender a demanda (ex: 0.01 = 1%)"
    )

    # =========================
    # Modo
    # =========================
    parser.add_argument(
        "--modo",
        type=str,
        default="mistura",
        choices=["mistura", "fonte_unica"],
        help="Modo de formulação: mistura (default) ou fonte_unica"
    )