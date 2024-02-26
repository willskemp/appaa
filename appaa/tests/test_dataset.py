from appaa.dataset import Dataset
import numpy as np
import pandas as pd
import os
from pathlib import Path


def test_obs_to_array():
    wd = Path.cwd()
    os.chdir(wd.parent)
    test_df = pd.read_csv('test_data.csv')
    test_dataset = Dataset(test_df)
    test_obs = test_dataset._to_obs_to_array(0)
    assert len(test_obs) == 1000
    assert type(test_obs) is np.ndarray
