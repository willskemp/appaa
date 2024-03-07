from appaa.analysis import ExperimentResults
from appaa.estimator import DifferenceInMeans
from appaa.data.test import load_data
import numpy as np

test_df = load_data()
test_df["variant"] = test_df.index
test_estimator = DifferenceInMeans()
test_analysis = ExperimentResults(
    data=test_df,
    estimator=test_estimator,
    randomisation_unit_col="variant",
    metric_col="Y",
    variant_col="variant",
)
test_analysis.comparisons(test_ids=[1], control_ids=[0])


def test_obs_to_array(analysis: ExperimentResults = test_analysis):
    test_obs = analysis._obs_to_array(0)
    assert len(test_obs) == 1000
    assert type(test_obs) is np.ndarray
