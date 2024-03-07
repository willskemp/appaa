# pip3 install '/Users/willkemp/Python/GitHub/appaa'

from appaa.effect_distribution import (
    ConstantEffect,
    UniformlyDistributedEffect,
    NormallyDistributedEffect,
)

constant = ConstantEffect(effect_size=50)
uniform = UniformlyDistributedEffect(-50, 50)
normal = NormallyDistributedEffect(mean=1000, std=50)

constant_effects = constant.add_effect(10)
uniform_effects = uniform.add_effect(10)
normal_effects = uniform.add_effect(10)

print(constant_effects)
print(uniform_effects)
print(normal_effects)
