from appaa.postanalysis import PostAnalysis
from appaa.estimator import DifferenceInMeans
from appaa.data.read_test_data import load_data

df = load_data()
df.head()

estimator = DifferenceInMeans(alpha=0.05, beta=0.8)
analyse = PostAnalysis(data=df,
                       test_ids=[1],
                       control_ids=[0],
                       estimator=estimator)
analyse.results()
