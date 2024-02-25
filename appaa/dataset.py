import pandas as pd


class Dataset:

    def __init__(self, data: pd.DataFrame, version_col: str):
        self.data = data

    def obs_test(self, id: any):
        return None

    def obs_control(self, id: any):
        return None
