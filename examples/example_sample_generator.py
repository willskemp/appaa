from appaa.data.sample_generator import NormalDistribution
from appaa.effect_distribution import ConstantEffect

test_cnt = 1
test_n = 10
control_cnt = 1
control_n = 10
effect_distribution = ConstantEffect(effect_size=10)
mean = 100
std = 5

normal_generator = NormalDistribution(
    test_cnt=test_cnt,
    test_n=test_n,
    control_cnt=control_cnt,
    control_n=control_n,
    effect_distribution=effect_distribution,
    mean=mean,
    std=std,
)

sampled_df = normal_generator.generate()

print(sampled_df)
