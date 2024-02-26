from appaa.dataset import Dataset
from appaa.data.read_test_data import load_data
import numpy as np

test_df = load_data()
test_dataset = Dataset(test_df)


def test_obs_to_array(test_dataset: Dataset = test_dataset):
    test_obs = test_dataset._obs_to_array(0)
    assert len(test_obs) == 1000
    assert type(test_obs) is np.ndarray


def test_obs():
    test_df = load_data()
    test_dataset = Dataset(test_df)
    test_dataset._obs(1, 0)
    assert len(test_dataset.Yt) == 1000
    assert type(test_dataset.Yt) is np.ndarray
    assert len(test_dataset.Yc) == 1000
    assert type(test_dataset.Yc) is np.ndarray

