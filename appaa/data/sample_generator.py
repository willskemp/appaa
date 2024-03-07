from abc import ABC, abstractmethod
from appaa.effect_distribution import EffectDistribution
import numpy as np
import pandas as pd


class SampleGenerator(ABC):

    def __init__(
        self,
        test_cnt: int,
        test_n: int,
        control_cnt: int,
        control_n: int,
        effect_distribution: EffectDistribution,
        **kwargs,
    ):
        self.id_cnt = test_cnt + control_cnt
        self.test_cnt = test_cnt
        self.test_n = test_n
        self.control_cnt = control_cnt
        self.control_n = control_n
        self.effect_distribution = effect_distribution

    @abstractmethod
    def generate(self):
        pass


class EmpiricalDistribution(SampleGenerator):

    def __init__(
        self,
        test_cnt: int,
        test_n: int,
        control_cnt: int,
        control_n: int,
        effect_distribution: EffectDistribution,
        data: pd.DataFrame,
        randomisation_unit_col: str,
    ):
        super().__init__(
            test_cnt=test_cnt,
            test_n=test_n,
            control_cnt=control_cnt,
            control_n=control_n,
            effect_distribution=effect_distribution,
        )
        self.data = data
        self.randomisation_unit_col = randomisation_unit_col

    def generate(self):
        simulated_df = pd.DataFrame(data=None)
        effect_sizes = self.effect_distribution.add_effect(self.test_cnt)
        id_cnt = self.test_cnt + self.control_cnt
        for i in range(0, id_cnt):
            sampled_df = self.data.sample(n=self.test_n, replace=True)
            if i < self.test_cnt:
                tmp_effect = np.ones(self.test_n) * effect_sizes[i]
                sampled_df["effect_size"] = tmp_effect
                sampled_id = np.ones(self.test_n) * i
            else:
                sampled_df["effect_size"] = np.zeros(self.control_n)
                sampled_id = np.ones(self.control_n) * i
            tmp_df = pd.DataFrame(data=sampled_df, index=sampled_id)
            simulated_df = pd.concat([simulated_df, tmp_df])

        return simulated_df


class NormalDistribution(SampleGenerator):

    def __init__(
        self,
        test_cnt: int,
        test_n: int,
        control_cnt: int,
        control_n: int,
        effect_distribution: EffectDistribution,
        mean: float,
        std: float,
    ):
        super().__init__(
            test_cnt=test_cnt,
            test_n=test_n,
            control_cnt=control_cnt,
            control_n=control_n,
            effect_distribution=effect_distribution,
        )
        self.mean = mean
        self.std = std

    def generate(self):
        simulated_df = pd.DataFrame(data=None)
        effect_sizes = self.effect_distribution.add_effect(self.test_cnt)
        id_cnt = self.test_cnt + self.control_cnt
        for i in range(0, id_cnt):
            if i < self.test_cnt:
                mean = self.mean + effect_sizes[i]
                std = self.std
                n = self.test_n
                tmp_Y = np.random.normal(loc=mean, scale=std, size=n)
                tmp_effect = np.ones(self.test_n) * effect_sizes[i]
                sampled_id = np.ones(self.test_n) * i
                sampled_dict = {'effect_size': tmp_effect, 'Y': tmp_Y}
                sampled_df = pd.DataFrame(data=sampled_dict, index=sampled_id)
            else:
                mean = self.mean
                std = self.std
                n = self.test_n
                tmp_Y = np.random.normal(loc=mean, scale=std, size=n)
                tmp_effect = np.ones(self.test_n) * effect_sizes[i]
                sampled_id = np.ones(self.test_n) * i
                sampled_dict = {'effect_size': tmp_effect, 'Y': tmp_Y}
                sampled_df = pd.DataFrame(data=sampled_dict, index=sampled_id)
            tmp_df = pd.DataFrame(data=sampled_df, index=sampled_id)
            simulated_df = pd.concat([simulated_df, tmp_df])

        return simulated_df
