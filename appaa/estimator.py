from abc import ABC, abstractmethod
import numpy as np
from scipy import stats
from typing import Any


class Estimator(ABC):

    def __init__(self, alpha: float, beta: float, **kwargs: Any):
        self.alpha = alpha
        self.beta = beta

    @abstractmethod
    def point_estimate(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        pass

    @abstractmethod
    def variance(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        pass

    @abstractmethod
    def std_error(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        pass

    @abstractmethod
    def confidence_interval(
        self, Yt: np.ndarray, Yc: np.ndarray
    ) -> tuple[float, float]:
        pass

    @abstractmethod
    def p_value(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        pass

    @abstractmethod
    def mde(self, Yt: np.ndarray, Yc: np.ndarray):
        pass

    @abstractmethod
    def power(self, Yt: np.ndarray, Yc: np.ndarray, estimated_effect: float):
        pass


class DifferenceInMeans(Estimator):

    def __init__(self, alpha: float = 0.05, beta: float = 0.8):
        super().__init__(alpha, beta)

    def point_estimate(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        mean_Yt = np.mean(Yt)
        mean_Yc = np.mean(Yc)
        return mean_Yt - mean_Yc

    def variance(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        nt = len(Yt)
        nc = len(Yc)
        var_Yt = np.var(Yt, ddof=1)
        var_Yc = np.var(Yc, ddof=1)
        return var_Yt / nt + var_Yc / nc

    def std_error(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        variance = self.variance(Yt, Yc)
        return np.sqrt(variance)

    def confidence_interval(
        self, Yt: np.ndarray, Yc: np.ndarray
    ) -> tuple[float, float]:
        point_estimate = self.point_estimate(Yt, Yc)
        std_error = self.std_error(Yt, Yc)
        critical_t = stats.t.ppf(1 - self._alpha, 10000)
        lb = point_estimate - (std_error * critical_t)
        ub = point_estimate + (std_error * critical_t)
        return (lb, ub)

    def t_value(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        return self.point_estimate(Yt, Yc) / self.std_error(Yt, Yc)

    def p_value(self, Yt: np.ndarray, Yc: np.ndarray) -> float:
        return stats.t.sf(np.abs(self.t_value(Yt, Yc)), 1) * 2

    def mde(self, Yt: np.ndarray, Yc: np.ndarray):
        critical_t = stats.t.ppf(1 - self.alpha, 10000)
        power_t = stats.t.ppf(self.beta, 10000)
        mde_t = critical_t + power_t
        return mde_t * self.std_error(Yt, Yc)

    def power(self, Yt: np.ndarray, Yc: np.ndarray, estimated_effect: float):
        critical_t = stats.t.ppf(1 - self.alpha, 10000)
        power_t = estimated_effect / self.std_error(Yt, Yc)
        mde_t = power_t - critical_t
        return stats.t.cdf(mde_t, 10000)
