from appaa.dataset import Dataset
from appaa.data.read_test_data import load_data
import numpy as np


def test_obs_to_array():
    test_df = load_data()
    test_dataset = Dataset(test_df)
    test_obs = test_dataset._obs_to_array(0)
    assert len(test_obs) == 1000
    assert type(test_obs) is np.ndarray
