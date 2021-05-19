from abc import ABCMeta, abstractmethod


class Character(ABCMeta):
    @abstractmethod
    def interact_with(self):
        pass


class Obstacle(ABCMeta):
    @abstractmethod
    def action(self):
        pass


class GamingWorld(ABCMeta):
    @abstractmethod
    def make_character(self):
        pass

    @abstractmethod
    def make_obstacle(self):
        pass
