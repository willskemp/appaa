from appaa.data.generator import NormalDistribution

generator = NormalDistribution(id_cnt=2, id_n=[50, 50], mu=100, sd=5)
print(generator._data)