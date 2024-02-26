import pandas as pd
from typing import Any


class Dataset:

    def __init__(self, data: pd.DataFrame, version_col: str):
        self.data = data

    def obs_test(self, id: Any):
        return None

    def obs_control(self, id: Any):
        return None
