from appaa.dataset import Dataset
from appaa.estimate import DifferenceInMeans
from appaa.data.read_test_data import load_data
import numpy as np

test_df = load_data()
test_dataset = Dataset(test_df)
test_dataset.obs(1, 0)
test_estimator = DifferenceInMeans(test_dataset)


def test_estimate(test_estimator: DifferenceInMeans = test_estimator):
    test_estimator.estimate()
    assert np.round(test_estimator.mean_Yt, 5) == 99.96336
    assert np.round(test_estimator.mean_Yc, 5) == 99.92445
