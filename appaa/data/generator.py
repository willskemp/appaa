import numpy as np
import pandas as pd


class Generator:

    def __init__(self, id_cnt: int, id_n: list[int]):
        sample_df = pd.DataFrame(data=None, columns=['Y'])
        for i in range(0, id_cnt):
            Y_tmp = np.zeros(id_n[i])
            id_tmp = np.ones(id_n[i]) * i
            tmp_df = pd.DataFrame(data=Y_tmp, index=id_tmp, columns=['Y'])
            sample_df = pd.concat([sample_df, tmp_df])
        self._id_cnt = id_cnt
        self._data = sample_df

    def add_effect_constant(self, test_cnt: int, lb: float, ub: float):
        np.random.uniform(low=lb, high=ub, size=test_cnt)

    def add_effect_normal(self, test_cnt: int, mu: float, sd: float):
        np.random.normal(loc=mu, scale=sd, size=test_cnt)

    def add_effect_uniform(self, test_cnt: int, lb: float, ub: float):
        np.random.uniform(low=lb, high=ub, size=test_cnt)


class NormalDistribution(Generator):

    def __init__(self, id_cnt: int, id_n: list[int], mu: float, sd: float):
        sample_df = pd.DataFrame(data=None, columns=['Y'])
        for i in range(0, id_cnt):
            Y_tmp = np.random.normal(loc=mu, scale=sd, size=id_cnt)
            id_tmp = np.ones(id_n[i]) * i
            tmp_df = pd.DataFrame(data=Y_tmp, index=id_tmp, columns=['Y'])
            sample_df = pd.concat([sample_df, tmp_df])
        self._id_cnt = id_cnt
        self._data = sample_df
