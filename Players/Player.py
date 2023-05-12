from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_next_move(self, board):
        pass

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
    