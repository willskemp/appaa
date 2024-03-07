from abc import ABC, abstractmethod
from appaa.estimator import Estimator
from itertools import product
import pandas as pd
from typing import Any


class Analysis(ABC):

    def __init__(
        self,
        data: pd.DataFrame,
        estimator: Estimator,
        randomisation_unit_col: str,
        metric_col: str,
        **kwargs: Any,
    ):
        self.data = data
        self.estimator = estimator
        self.randomisation_unit_col = randomisation_unit_col
        self.metric_col = metric_col

    def _obs_to_array(self, id: float) -> list[float]:
        df = self.data.loc[self.data.index == id]
        return df.to_numpy()

    def comparisons(self, test_ids: list[int], control_ids: list[int]):
        self.comparisons = list(product(test_ids, control_ids))

    @abstractmethod
    def estimate_results(self) -> pd.DataFrame:
        pass


class ExperimentResults(Analysis):

    def __init__(
        self,
        data: pd.DataFrame,
        estimator: Estimator,
        randomisation_unit_col: str,
        metric_col: str,
        variant_col: str,
        **kwargs: Any,
    ):
        super().__init__(data, estimator, randomisation_unit_col, metric_col)
        self.variant_col = variant_col
        self.data.set_index(variant_col)

    def estimate_results(self) -> pd.DataFrame:
        estimated_results_list = []
        for pair in self.comparisons:
            test_id = pair[0]
            control_id = pair[1]
            Yt = self._obs_to_array(test_id)
            Yc = self._obs_to_array(control_id)

            assignment_dict = {}
            estimates_dict = {}
            estimated_results_dict = {}
            assignment_dict = {
                "test_id": test_id,
                "control_id": control_id,
            }
            estimates_dict = self.estimator.estimate_results(Yt, Yc)
            estimated_results_dict = assignment_dict | estimates_dict
            estimated_results_list.append(estimated_results_dict)
        estimated_results_df = pd.DataFrame(data=estimated_results_list)
        return estimated_results_df
