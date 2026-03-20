def parse_fontes(
    entradas: list[str],
    fontes_yaml: dict
) -> list[tuple[str, dict]]:

    fontes = []

    for entrada in entradas:

        # =========================
        # Caso 1: fonte do YAML
        # =========================
        entrada_norm = entrada.strip().lower()

        # procurar ignorando case
        match = next(
            (k for k in fontes_yaml if k.lower() == entrada_norm),
            None
        )

        if match:
            fontes.append((match.lower(), fontes_yaml[match]))
            continue

        # =========================
        # Caso 2: fonte custom genérica
        # =========================
        try:
            if ":" not in entrada:
                raise ValueError()

            nome, garantias_str = entrada.split(":", 1)
            garantias = {}

            for item in garantias_str.split(","):
                if "=" not in item:
                    raise ValueError()

                k, v = item.split("=", 1)
                garantias[k.strip()] = float(v)

            fontes.append((
                nome.strip().lower(),
                {
                    "nome": nome.strip(),
                    "garantias": garantias
                }
            ))

        except Exception:
            raise ValueError(
                f"Formato inválido de fonte: '{entrada}'.\n\n"
                "Formatos válidos:\n"
                "  • Nome de fonte do YAML:\n"
                "      ureia\n"
                "      calcario\n\n"
                "  • Fonte customizada:\n"
                "      nome:N=valor,P2O5=valor,K2O=valor\n"
                "      nome:prnt=80\n"
                "      Exemplo: meu_adubo:N=10,P2O5=20,K2O=10\n"
            )

    return fontes

def resolver_fontes(
    entradas: list[str] | None,
    fontes_yaml: dict
) -> list[tuple[str, dict]]:

    # usuário não passou nada → usa padrão do YAML
    if entradas is None:
        return list(fontes_yaml.items())

    # usuário passou lista vazia → erro explícito
    if not entradas:
        raise ValueError(
            "Lista de fontes vazia.\n"
            "Informe ao menos uma fonte ou não passe o parâmetro."
        )

    return parse_fontes(entradas, fontes_yaml)
