import numpy as np


def average_treatment_effect_point_estimate(obs_test, obs_control):
    return np.mean(obs_test) - np.mean(obs_control)


def average_treatment_effect_variance(obs_test, obs_control):
    n_test = len(obs_test)
    n_control = len(obs_control)

    return (np.var(obs_test) / n_test) + (np.var(obs_control) / n_control)
