from fertpy.infra.loaders.fonte_loader import carregar_fontes
from fertpy.infra.parsing.fontes import resolver_fontes
from fertpy.core.factories.criador_fertilizante import criar_fertilizante
from fertpy.core.engine.formulacao_adubacao import formular


class FormulacaoAdubacao:

    def __init__(self, boletim="boletim_100"):
        self.boletim = boletim

    def calcular(
            self,
            demanda: dict,
            entradas_fontes: list,
            precos: dict | None = None,
            fretes: dict | None = None,
            solver: str = "quantidade_minima",
            tolerancia: float | None = 0.05,
            tol_inf: float | None = None,
            tol_sup: float | None = None,
            modo: str = "mistura"
    ):
        #========================
        # Carregar fontes padrão
        #========================
        fontes_yaml = carregar_fontes(self.boletim, tipo="adubacao")

        #=================
        # Resolver fontes
        #=================
        fontes_resolvidas = resolver_fontes(
            entradas_fontes,
            fontes_yaml
        )

        fontes = [
            criar_fertilizante(nome, dados)
            for nome, dados in fontes_resolvidas
        ]

        #=================
        # Execultar formulação
        #=================
        resultado = formular(
            demanda=demanda,
            fontes=fontes,
            precos=precos,
            fretes=fretes,
            solver=solver,
            tolerancia=tolerancia,
            tol_inf=tol_inf,
            tol_sup=tol_sup,
            modo=modo
        )

        return {
            "doses": resultado["doses"],
            "unidade": resultado.get("unidade", "kg/ha"),
            "observacoes": resultado.get("observacoes", []),
            "custo_total": resultado.get("custo_total"),
            "custo_por_fonte": resultado.get("custo_por_fonte"),
        }
