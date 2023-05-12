import random

from Players.Player import Player


class RandomPlayer(Player):

    def __init__(self, color):
        super().__init__(color)
        self.rand = random.Random()

    def get_next_move(self, board):
        moves = board.get_moves(self.color)
        n = len(moves)
        if n == 0:
            return None
        k = self.rand.randint(0, n-1)
        return moves[k]
