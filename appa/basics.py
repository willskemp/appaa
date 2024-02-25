import numpy as np


class DifferenceInMeans:
    def __init__(self, obs_test, obs_control):
        self.obs_test = obs_test
        self.obs_control = obs_control

    def est(self):
        return np.mean(self.obs_test) - np.mean(self.obs_control)

    def var(self):
        n_test = len(self.obs_test)
        n_control = len(self.obs_control)
        var_test = np.var(self.obs_test) / n_test
        var_control = np.var(self.obs_control) / n_control
        return var_test + var_control
