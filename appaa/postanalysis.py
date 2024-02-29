from appaa.estimator import Estimator
from itertools import product
import pandas as pd


class PostAnalysis:

    def __init__(
        self,
        data: pd.DataFrame,
        test_ids: list[int],
        control_ids: list[int],
        estimator: Estimator,
    ):
        self._data = data
        self._comparisons = list(product(test_ids, control_ids))
        self.estimator = estimator

    def _obs_to_array(self, id: float) -> list[float]:
        df = self._data.loc[self._data.index == id]
        return df.to_numpy()

    def results(self) -> pd.DataFrame:
        results_list = []
        results_dict = {}
        for pair in self._comparisons:
            test_id = pair[0]
            control_id = pair[1]
            Yt = self._obs_to_array(test_id)
            Yc = self._obs_to_array(control_id)
            point_estimate = self.estimator.point_estimate(Yt, Yc)
            variance = self.estimator.variance(Yt, Yc)
            std_error = self.estimator.std_error(Yt, Yc)
            confidence_interval = self.estimator.confidence_interval(Yt, Yc)
            p_value = self.estimator.p_value(Yt, Yc)
            results_dict = {
                "test_id": test_id,
                "control_id": control_id,
                "point_estimate": point_estimate,
                "variance": variance,
                "std_error": std_error,
                "confidence_interval": confidence_interval,
                "p_value": p_value,
            }
            results_list.append(results_dict)
        results_df = pd.DataFrame(data=results_list)
        return results_df
