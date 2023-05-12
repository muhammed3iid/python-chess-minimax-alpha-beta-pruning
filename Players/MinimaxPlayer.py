from Minimax.Minimax import Minimax
from Players.Player import Player


class MinimaxPLayer(Player):

    def __init__(self, color, max_depth):
        super().__init__(color)
        self.minimax = Minimax(color, max_depth)

    def get_next_move(self, board):
        # moves = board.get_moves(self.color)
        move = self.minimax.decision(board)
        return move
