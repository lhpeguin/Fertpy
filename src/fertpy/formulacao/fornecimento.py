from fertpy.infra.loaders.fonte_loader import carregar_fontes
from fertpy.infra.parsing.fontes import resolver_fontes
from fertpy.core.factories.criador_fertilizante import criar_fertilizante
from fertpy.core.engine.nutriente_fornecido import nutrientes_fornecidos


class NutrientesFornecidos:

    def __init__(self, boletim="boletim_100"):
        self.boletim = boletim

    def calcular(
        self,
        entrada_fonte: str,
        dose: float
    ):

        fontes_yaml = carregar_fontes(self.boletim)

        fontes_resolvidas = resolver_fontes(
            [entrada_fonte],
            fontes_yaml
        )

        nome, dados = fontes_resolvidas[0]

        fert = criar_fertilizante(nome, dados)

        return nutrientes_fornecidos(
            dose=dose,
            fertilizer=fert
        ), fert
