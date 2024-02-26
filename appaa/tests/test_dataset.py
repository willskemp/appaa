from appaa.dataset import Dataset
import numpy as np
import pandas as pd


def test_obs_to_array():
    import os
    fname = os.path.join(os.path.dirname(__file__), 'test_data.csv')
    test_df = pd.read_csv(fname)
    test_dataset = Dataset(test_df)
    test_obs = test_dataset._obs_to_array(0)
    assert len(test_obs) == 1000
    assert type(test_obs) is np.ndarray
