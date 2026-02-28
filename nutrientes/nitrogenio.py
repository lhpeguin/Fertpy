from fertpy.infra.loaders.yaml_loader import carregar_modelo
from fertpy.infra.parsing.modelo_agronomico import parse_modelo_agronomico
from fertpy.core.engine.avaliador import Avaliador


class Nitrogenio:

    def __init__(self, cultura: str, finalidade: str):

        yaml = carregar_modelo(
            "boletim_100",
            cultura,
            f"{cultura}_{finalidade}_nitrogenio"
        )["nitrogenio"]
        
        parseado = parse_modelo_agronomico(yaml)
        self.modelo = parseado

    def calcular(
            self,
            classe_resp_N: str,
            produtividade: float
    ):
        
        contexto = {
            "classe_resp_N": classe_resp_N,
            "produtividade": produtividade
        }

        return Avaliador.avaliar(
            criterios=self.modelo.criterios,
            contexto=contexto,
            nutriente=self.modelo.nutriente,
            unidade=self.modelo.unidade_saida,
            observacoes=None,
            fonte=self.modelo.fonte_referencia
        )
