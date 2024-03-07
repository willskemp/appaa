from abc import ABC, abstractmethod


class Simulation(ABC):

    @abstractmethod
    def __init__(self, iter: int):
        pass
