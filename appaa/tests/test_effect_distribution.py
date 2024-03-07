from appaa.effect_distribution import (
    ConstantEffect,
    UniformlyDistributedEffect,
    NormallyDistributedEffect,
)
import numpy as np


def test_constant_effect_add_effect():
    constant = ConstantEffect(effect_size=50)
    constant_effects = constant.add_effect(1000)
    assert len(constant_effects) == 1000
    assert np.mean(constant_effects) == 50


def test_uniform_effect_add_effect():
    uniform = UniformlyDistributedEffect(lb=-50, ub=50)
    uniform_effects = uniform.add_effect(2000)
    assert len(uniform_effects) == 2000
    assert np.round(np.mean(uniform_effects), 5) == 0.01731


def test_normal_effect_add_effect():
    normal = NormallyDistributedEffect(mean=1000, std=50)
    normal_effects = normal.add_effect(3000)
    assert len(normal_effects) == 3000
    assert np.round(np.mean(normal_effects), 5) == 1000.65173
