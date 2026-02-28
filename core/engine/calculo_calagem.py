class CalagemEngine:

    @staticmethod
    def calcular(
        v1: float,
        ctc: float,
        v2: float,
        prnt: float,
        dose_maxima: float | None = None,
        dose_minima: float | None = None
    ) -> float:

        nc = (ctc * (v2 - v1)) / (10 * prnt)

        if nc <= 0:
            return 0.0

        if dose_maxima is not None and nc > dose_maxima:
            nc = dose_maxima

        if dose_minima is not None and nc < dose_minima:
            return 0.0

        return round(nc, 2)