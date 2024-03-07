from abc import ABC, abstractmethod
import numpy as np
from typing import Any


class EffectDistribution(ABC):
    @abstractmethod
    def __init__(self, test_cnt: int, **kwargs: Any):
        pass

    @abstractmethod
    def add_effect(self):
        pass


class ConstantEffect(EffectDistribution):

    def __init__(self, id_cnt: int, effect_size: float):
        self.effect_size = effect_size

    def add_effect(self, test_cnt: int) -> np.ndarray:
        effect_sizes = self.effect_size * np.ones(test_cnt)
        return effect_sizes


class UniformlyDistributedEffect(EffectDistribution):

    def __init__(self, lb: float, ub: float):
        self.lb = lb
        self.ub = ub

    def add_effect(self, test_cnt: int) -> np.ndarray:
        np.random.seed(32)
        lb = self.lb
        ub = self.ub
        effect_sizes = np.random.uniform(low=lb, high=ub, size=test_cnt)
        return effect_sizes


class NormallyDistributedEffect(EffectDistribution):

    def __init__(self, mean: float, std: float):
        self.mean = mean
        self.std = std

    def add_effect(self, test_cnt: int) -> np.ndarray:
        np.random.seed(32)
        mean = self.mean
        std = self.std
        effect_sizes = np.random.normal(loc=mean, scale=std, size=test_cnt)
        return effect_sizes
