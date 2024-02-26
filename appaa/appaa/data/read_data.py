import os
import pandas as pd


def get_data():
    fname = os.path.join(os.path.dirname(__file__), 'test_data.csv')
    data = pd.read_csv(fname, index_col=0)
    return data
