class CalagemEngine:

    @staticmethod
    def calcular(
        v1: float,
        ctc: float,
        v2: float,
        prnt: float
    ) -> float:
        # modo atual (fonte única)
        nc = (ctc * (v2 - v1)) / (10 * prnt)

        if nc <= 0:
            return 0.0

        return round(nc, 2)

    @staticmethod
    def calcular_nc_base(
        v1: float,
        ctc: float,
        v2: float,
        dose_maxima: float | None = None,
        dose_minima: float | None = None
    ) -> float:

        nc = (ctc * (v2 - v1)) / 100  # PRNT = 100%

        if nc <= 0:
            return 0.0

        return nc
