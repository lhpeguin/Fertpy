from fertpy.infra.loaders.fonte_loader import carregar_fontes
from fertpy.infra.loaders.correcao_loader import carregar_modelo_correcao
from fertpy.infra.parsing.fontes import resolver_fontes
from fertpy.infra.parsing.calagem_parser import parse_calagem_model
from fertpy.core.factories.criador_corretivo import criar_corretivo
from fertpy.core.engine.formulacao_calagem import formular_calagem


class FormulacaoCalagem:

    def __init__(self, boletim="boletim_100"):
        self.boletim = boletim

    def calcular(
        self,
        cultura: str,
        v_atual: float,
        ctc: float,
        entradas_fontes: list,
        precos: dict | None = None,
        fretes: dict | None = None,
        solver: str = "quantidade_minima",
        tolerancia: float = 0.05,
        tol_inf: float | None = None,
        tol_sup: float | None = None
    ):

        # ========================
        # Carregar modelo de cultura
        # ========================
        raw = carregar_modelo_correcao(
            self.boletim,
            cultura
        )["calagem"]

        modelo = parse_calagem_model(raw)

        V_desejado = modelo.parametros.v2_desejado

        # ========================
        # Carregar fontes
        # ========================
        fontes_yaml = carregar_fontes(
            self.boletim,
            tipo="calagem"
        )

        fontes_resolvidas = resolver_fontes(
            entradas_fontes,
            fontes_yaml
        )

        fontes = [
            criar_corretivo(nome, dados)
            for nome, dados in fontes_resolvidas
        ]

        # ========================
        # Execução
        # ========================
        resultado = formular_calagem(
            V_atual=v_atual,
            V_desejado=V_desejado,
            CTC=ctc,
            fontes=fontes,
            precos=precos,
            fretes=fretes,
            solver=solver,
            tolerancia=tolerancia,
            tol_inf=tol_inf,
            tol_sup=tol_sup,
            modelo=modelo
        )

        return {
            "doses": resultado["doses"],
            "unidade": "t/ha",
            "observacoes": resultado.get("observacoes", []),
            "custo_total": resultado.get("custo_total"),
            "custo_por_fonte": resultado.get("custo_por_fonte"),
        }