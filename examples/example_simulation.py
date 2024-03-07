from appaa.data.sample_generator import NormalDistribution
from appaa.effect_distribution import ConstantEffect
from appaa.simulation import Simulation

# Simulation Parameters
iterations = 10  # No. of experiment scenarios to be simulated

# Simulated Experiment Design
test_cnt = 1
test_n = 10
control_cnt = 1
control_n = 10

# Simulated Data Distribution
mean = 100
std = 5

# Simulated Effect Distribution
effect_distribution = ConstantEffect(effect_size=10)


sample_generator = NormalDistribution(
    test_cnt=test_cnt,
    test_n=test_n,
    control_cnt=control_cnt,
    control_n=control_n,
    effect_distribution=effect_distribution,
    mean=mean,
    std=std,
)

simulation = Simulation(
    iterations=iterations,
    sample_generator=sample_generator,
)

print(simulation.simulated_data)
len(simulation.simulated_data)
