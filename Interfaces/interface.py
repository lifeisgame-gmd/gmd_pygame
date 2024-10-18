from abc import abstractmethod


class Interface:
    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass

    @classmethod
    def deactivate(self):
        from SceneManager import SceneManager
        SceneManager.ui = None