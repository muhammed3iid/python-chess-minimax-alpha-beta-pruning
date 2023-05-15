from Move import Move
from Pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.value = 3

    def __str__(self):
        if self.color == Piece.WHITE:
            return '\u2658'
        else:
            return '\u265E'

    def clone(self):
        return Knight(self.color)

    def get_moves(self, board, x, y):
        moves = []
        # NNE
        if self.is_valid(x + 1, y + 2) and (not board.get_tile(x + 1, y + 2).is_occupied() or (
                board.get_tile(x + 1, y + 2).is_occupied() and board.get_tile(x + 1,
                                                                              y + 2).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y + 2))

        # ENE
        if self.is_valid(x + 2, y + 1) and (not board.get_tile(x + 2, y + 1).is_occupied() or (
                board.get_tile(x + 2, y + 1).is_occupied() and board.get_tile(x + 2,
                                                                              y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 2, y + 1))

        # ESE
        if self.is_valid(x + 2, y - 1) and (not board.get_tile(x + 2, y - 1).is_occupied() or (
                board.get_tile(x + 2, y - 1).is_occupied() and board.get_tile(x + 2,
                                                                              y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 2, y - 1))

        # SSE
        if self.is_valid(x + 1, y - 2) and (not board.get_tile(x + 1, y - 2).is_occupied() or (
                board.get_tile(x + 1, y - 2).is_occupied() and board.get_tile(x + 1,
                                                                              y - 2).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y - 2))

        # SSW
        if self.is_valid(x - 1, y - 2) and (not board.get_tile(x - 1, y - 2).is_occupied() or (
                board.get_tile(x - 1, y - 2).is_occupied() and board.get_tile(x - 1,
                                                                              y - 2).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y - 2))

        # WSW
        if self.is_valid(x - 2, y - 1) and (not board.get_tile(x - 2, y - 1).is_occupied() or (
                board.get_tile(x - 2, y - 1).is_occupied() and board.get_tile(x - 2,
                                                                              y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 2, y - 1))

        # WNW
        if self.is_valid(x - 2, y + 1) and (not board.get_tile(x - 2, y + 1).is_occupied() or (
                board.get_tile(x - 2, y + 1).is_occupied() and board.get_tile(x - 2,
                                                                           y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 2, y + 1))

        # NNW
        if self.is_valid(x - 1, y + 2) and (not board.get_tile(x - 1, y + 2).is_occupied() or (
                board.get_tile(x - 1, y + 2).is_occupied() and board.get_tile(x - 1,
                                                                           y + 2).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y + 2))

        return moves
