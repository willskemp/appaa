# pip3 install '/Users/willkemp/Python/GitHub/appaa'

from appaa.analysis import ExperimentResults
from appaa.estimator import DifferenceInMeans
from appaa.data.test import load_data

df = load_data()
df['variant'] = df.index

estimator = DifferenceInMeans(alpha=0.05, beta=0.8)
analyse = ExperimentResults(
    data=df,
    estimator=estimator,
    randomisation_unit_col='variant',
    metric_col='Y',
    variant_col='variant',
)
analyse.comparisons(test_ids=[1], control_ids=[0])
output = analyse.estimate_results()
print(output.head())
