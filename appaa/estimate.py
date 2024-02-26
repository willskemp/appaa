from dataset import Dataset
import numpy as np


class DifferenceInMeans:

    def __init__(self, dataset: Dataset):
        self.Yt = dataset.Yt
        self.Yc = dataset.Yc
        self.nt = len(dataset.Yt)
        self.nc = len(dataset.Yc)

    def estimate(self) -> float:
        self.mean_Yt = np.mean(self.Yt)
        self.mean_Yc = np.mean(self.Yc)
        return self.mean_Yt - self.mean_Yc

    def variance(self) -> float:
        self.var_Yt = np.var(self.Yt, ddof=1)
        self.var_Yc = np.var(self.Yc, ddof=1)
        return self.var_Yt / self.nt + self.var_Yc / self.nc

    def confidence_interval(self, alpha=0.05) -> tuple[float, float]:
        return None
