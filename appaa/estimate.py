import numpy as np


class DifferenceInMeans:

    def __init__(self, obs_test: list[float], obs_control: list[float]):
        self.obs_test = obs_test
        self.obs_control = obs_control

    def est(self) -> float:
        return np.mean(self.obs_test) - np.mean(self.obs_control)

    def var(self) -> float:
        n_test = len(self.obs_test)
        n_control = len(self.obs_control)
        var_test = np.var(self.obs_test, ddof=1) / n_test
        var_control = np.var(self.obs_control, ddof=1) / n_control
        return var_test + var_control

    def analytic_ci(self, alpha=0.05) -> tuple[float, float]:
        return None

    def bootstrap_ci(self, alpha=0.05, iterations=100) -> tuple[float, float]:
        return None


class RatioOfMeans:

    def __init__(self, obs_test: list[float], obs_control: list[float]):
        self.obs_test = obs_test
        self.obs_control = obs_control

    def est(self) -> float:
        return np.mean(self.obs_test) - np.mean(self.obs_control)

    def var(self) -> float:
        n_test = len(self.obs_test)
        n_control = len(self.obs_control)
        var_test = np.var(self.obs_test, ddof=1) / n_test
        var_control = np.var(self.obs_control, ddof=1) / n_control
        return var_test + var_control

    def analytic_ci(self, alpha=0.05) -> tuple[float, float]:
        return None

    def bootstrap_ci(self, alpha=0.05, iterations=100) -> tuple[float, float]:
        return None
