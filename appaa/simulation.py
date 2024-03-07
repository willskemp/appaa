from abc import ABC, abstractmethod
from appaa.analysis import ExperimentResults
from appaa.estimator import Estimator
from appaa.data.sample_generator import SampleGenerator
import pandas as pd


class Simulation(ABC):

    @abstractmethod
    def __init__(
        self,
        iterations: int,
        sample_generator: SampleGenerator,
    ):
        self.simulated_data = pd.DataFrame(data=None)
        for i in range(0, self.iterations):
            tmp_df = self.sample_generator.generate()
            tmp_df["iteration"] = i
            self.simulated_df = pd.concat([self.simulated_data, tmp_df])

    def analyse(self, estimator: Estimator):
        self.simulated_analysis = pd.DataFrame(data=None)
        for i in range(0, self.iterations):
            tmp_df = self.simulated_df[self.simulated_df.iteration == i]
            experiment = ExperimentResults(
                data=tmp_df, estimator=estimator, metric_col="", variant_col=""
            )
            test_cnt = self.sample_generator.test_cnt
            control_cnt = self.sample_generator.control_cnt
            test_ids = [i for i in range(0, test_cnt)]
            control_ids = [i for i in range(test_cnt, test_cnt + control_cnt)]
            experiment.comparisons(test_ids=test_ids, control_ids=control_ids)
            self.simulated_analysis = pd.concat([experiment.analyse(), tmp_df])
        return self.simulated_analysis
