from appaa.data.sample_generator import NormalDistribution
from appaa.effect_distribution import ConstantEffect
from appaa.estimator import DifferenceInMeans
from appaa.simulation import Simulation
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

sns.displot(experiment_df, x='t_value', stat='probability')
sns.displot(np.random.normal(0, 1, 1000), stat='probability', kind='kde')
plt.show()

sns.distplot(experiment_df['t_value'], hist=False)
sns.distplot(np.random.normal(0, 1, 500), hist=False)
plt.show()
# ax = sns.histplot(experiment_df, kde=False, stat='probability')

# calculate the pdf
# x0, x1 = ax.get_xlim()  # extract the endpoints for the x-axis
# x_pdf = np.linspace(x0, x1, 100)
# y_pdf = scipy.stats.norm.pdf(x_pdf)

# ax.plot(x_pdf, y_pdf, 'r', lw=2, label='pdf')
# ax.legend()
