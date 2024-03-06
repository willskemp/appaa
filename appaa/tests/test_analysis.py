from appaa.analysis import Analysis
from appaa.estimator import DifferenceInMeans
from appaa.data.test import load_data
import numpy as np

test_df = load_data()
test_estimator = DifferenceInMeans()
test_analysis = Analysis(
    data=test_df, test_ids=[1], control_ids=[0], estimator=test_estimator
)


def test_obs_to_array(analysis: Analysis = test_analysis):
    test_obs = analysis._obs_to_array(0)
    assert len(test_obs) == 1000
    assert type(test_obs) is np.ndarray
