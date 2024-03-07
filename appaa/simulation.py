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
        pass

    def simulate(self):
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
            self.simulated_analysis = pd.concat([experiment.analyse(), tmp_df])
        return self.simulated_analysis

    def check_stat_sig():
        pass
