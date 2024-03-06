# pip3 install '/Users/willkemp/Python/GitHub/appaa'

from appaa.estimator import DifferenceInMeans
from appaa.data.test import load_data

df = load_data()


df.loc[df.index == id].to_numpy()
estimator = DifferenceInMeans(alpha=0.05, beta=0.8)
Yt = df.loc[df.index == 1].to_numpy()
Yc = df.loc[df.index == 0].to_numpy()
mde = estimator.mde(Yt, Yc)
power = estimator.power(Yt, Yc, mde)

print(mde)
print(power)
