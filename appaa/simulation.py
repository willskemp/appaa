from appaa.analysis import ExperimentResults
from appaa.estimator import Estimator
from appaa.data.sample_generator import SampleGenerator
import pandas as pd
import progressbar


class Simulation:

    def __init__(
        self,
        iterations: int,
        sample_generator: SampleGenerator,
    ):
        self.iterations = iterations
        self.sample_generator = sample_generator
        self.simulated_data = pd.DataFrame(data=None)
        with progressbar.ProgressBar(max_value=iterations) as bar:
            for i in range(0, iterations):
                tmp_df = self.sample_generator.generate()
                tmp_df["iteration"] = i
                self.simulated_data = pd.concat([self.simulated_data, tmp_df])
                bar.update(i)

    def analyse(self, estimator: Estimator):
        self.simulated_analysis = pd.DataFrame(data=None)
        with progressbar.ProgressBar(max_value=self.iterations) as bar:
            for i in range(0, self.iterations):
                tmp_df = self.simulated_data[
                    self.simulated_data.iteration == i
                    ]
                experiment = ExperimentResults(
                    data=tmp_df,
                    estimator=estimator,
                    metric_col="Y",
                    variant_col="variant",
                )
                test_cnt = self.sample_generator.test_cnt
                control_cnt = self.sample_generator.control_cnt
                id_cnt = test_cnt + control_cnt
                test_ids = [i for i in range(0, test_cnt)]
                control_ids = [i for i in range(test_cnt, id_cnt)]
                experiment.comparisons(test_ids, control_ids)
                results_df = experiment.estimate_results()
                simulated_df = self.simulated_analysis
                self.simulated_analysis = pd.concat([simulated_df, results_df])
                bar.update(i)
        return self.simulated_analysis
