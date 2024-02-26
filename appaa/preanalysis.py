from appaa.estimator import Estimator
import pandas as pd


class PreAnalysis:

    def __init__(
        self,
        data: pd.DataFrame,
        estimator: Estimator,
    ):
        self._data = data
        self.estimator = estimator

    def _obs_to_array(self, id: float) -> list[float]:
        df = self._data.loc[self._data.index == id]
        return df.to_numpy()
