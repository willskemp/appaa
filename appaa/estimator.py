import numpy as np
from scipy import stats


class Estimator:

    def __init__(self):
        self._alpha = 0.05
        self._beta = 0.8

    def _point_estimate(Yt, Yc) -> float:
        return 0.0

    def _variance(Yt, Yc, nt, nc) -> float:
        return 0.0

    def _std_error(self, Yt, Yc, nt, nc) -> float:
        return 0.0

    def _confidence_interval(self) -> tuple[float, float]:
        return (0.0, 0.0)

    def _p_values(self) -> float:
        return 0.0


class DifferenceInMeans(Estimator):

    def __init__(self, alpha: float, beta: float):
        self._alpha = 0.05
        self._beta = 0.8

    def _point_estimate(Yt, Yc) -> float:
        mean_Yt = np.mean(Yt)
        mean_Yc = np.mean(Yc)
        return mean_Yt - mean_Yc

    def _variance(Yt, Yc) -> float:
        nt = len(Yt)
        nc = len(Yc)
        var_Yt = np.var(Yt, ddof=1)
        var_Yc = np.var(Yc, ddof=1)
        return var_Yt / nt + var_Yc / nc

    def _std_error(self, Yt, Yc) -> float:
        variance = self.variance(Yt, Yc)
        return np.sqrt(variance)

    def _confidence_interval(self, Yt, Yc) -> tuple[float, float]:
        point_estimate = self._point_estimate(Yt, Yc)
        std_error = self._std_error(self, Yt, Yc)
        critical_value = stats.t.ppf(1 - self._alpha, 10000)
        lb = point_estimate - (std_error * critical_value)
        ub = point_estimate + (std_error * critical_value)
        return (lb, ub)

    def _p_values(self, Yt, Yc) -> float:
        point_estimate = self._point_estimate(Yt, Yc)
        std_error = self._std_error(self, Yt, Yc)
        t_value = point_estimate / std_error
        return stats.t.sf(np.abs(t_value), 1) * 2
