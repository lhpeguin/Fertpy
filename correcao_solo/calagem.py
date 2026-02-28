from fertpy.infra.loaders.yaml_loader import carregar_modelo
from fertpy.core.engine.calculo_calagem import CalagemEngine


class Calagem:

    def __init__(self, cultura: str):

        yaml = carregar_modelo(
            "boletim_100",
            cultura,
            f"{cultura}_calagem"
        )["calagem"]

        self.modelo = yaml

    def calcular(
        self,
        v_atual: float,
        ctc: float,
        prnt: float | None = None
    ) -> float:

        parametros = self.modelo["parametros"]
        limites = self.modelo.get("limites", {})

        return CalagemEngine.calcular(
            v1=v_atual,
            ctc=ctc,
            v2=parametros["v2_desejado"],
            prnt=prnt or parametros["prnt_padrao"],
            dose_maxima=limites.get("dose_maxima"),
            dose_minima=limites.get("dose_minima")
        )
