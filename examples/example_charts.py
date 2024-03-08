from appaa.data.sample_generator import NormalDistribution
from appaa.effect_distribution import ConstantEffect
from appaa.estimator import DifferenceInMeans
from appaa.simulation import Simulation
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Simulation Parameters
iterations = 2500  # No. of experiment scenarios to be simulated

# Simulated Experiment Design
test_cnt = 1
test_n = 500
control_cnt = 1
control_n = 500

# Simulated Data Distribution
mean = 100
std = 5

# Estimator
estimator = DifferenceInMeans(alpha=0.05, beta=0.8)

# Simulated Effect Distribution
effect_distribution = ConstantEffect(effect_size=0)


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

experiment_df = simulation.analyse(estimator=estimator)

kde1 = stats.gaussian_kde(experiment_df["t_value"].to_numpy())
kde2 = stats.gaussian_kde(np.random.normal(0, 1, 2500))
xx = np.linspace(-4, 4, 1000)

fig, ax = plt.subplots(figsize=(16, 8))
ax.set_title("Simulated t-distribution vs. N(0, 1)")
ax.hist(
    x=experiment_df["t_value"].to_numpy(),
    density=True,
    bins=50,
    color="skyblue",
    label="Empirical",
)
ax.hist(
    x=np.random.normal(0, 1, 2500),
    density=True,
    bins=50,
    color="orange",
    label="N(0, 1)",
)
ax.plot(xx, kde1(xx), color='skyblue')
ax.plot(xx, kde2(xx), color='orange')
plt.xlim(-4, 4)
plt.ylim(0, 0.55)
plt.legend()
plt.show()
