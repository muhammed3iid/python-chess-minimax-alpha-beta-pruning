from Minimax.Minimax import Minimax
from Players.Player import Player


class MinimaxPlayer(Player):

    def __init__(self, color, max_depth):
        super().__init__(color)
        self.minimax = Minimax(color, max_depth)

    def get_next_move(self, board):
        move = self.minimax.decision(board)
        return move
