from abc import ABC, abstractmethod


class Piece(ABC):

    WHITE = True
    BLACK = False

    def __init__(self, color):
        self.color = color
        self.value = 0

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value

    @staticmethod
    def is_valid(x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False
        else:
            return True

    @abstractmethod
    def get_moves(self, board, x, y):
        pass

    @abstractmethod
    def clone(self):
        pass
