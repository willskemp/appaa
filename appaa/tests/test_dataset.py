import dataset
import numpy as np
import pandas as pd
import os
from pathlib import Path

wd = Path.cwd()
os.chdir(wd.parent)
test_df = pd.read_csv('./data/test_data.csv')
dataset = Dataset(test_df)

def test_obs_to_array():
    test_obs = dataset._to_obs_to_array(0)
    assert len(test_obs) == 1000
    assert type(test_obs) is np.array
