import pandas as pd


class Dataset:

    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def _obs_to_array(self, id: float) -> list[float]:
        tmp = self.dataset.loc(
            self.dataset.index == id
        )
        return tmp.to_numpy()

    def _obs(self, Yt_id: int, Yc_id: int):
        self.Yt = self._obs_to_array(Yt_id)
        self.Yc = self._obs_to_array(Yc_id)
