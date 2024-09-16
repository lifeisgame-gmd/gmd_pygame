from abc import abstractmethod


class Interface:
    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def __init__(self):
        pass