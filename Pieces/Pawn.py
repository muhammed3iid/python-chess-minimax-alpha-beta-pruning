from Move import Move
from Pieces.Piece import Piece


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.value = 1

    def __str__(self):
        if self.color == Piece.WHITE:
            return "P"
        else:
            return "p"

    def clone(self):
        return Pawn(self.color)

    def get_moves(self, b, x, y):
        moves = []
        if self.color == Piece.WHITE:
            # forward
            if self.is_valid(x, y + 1) \
                    and not b.get_tile(x, y + 1).is_occupied():
                moves.append(Move(x, y, x, y + 1))
            # kill diagonally
            if self.is_valid(x + 1, y + 1) \
                    and b.get_tile(x + 1, y + 1).is_occupied() \
                    and b.get_tile(x + 1, y + 1).get_piece().get_color() != self.color:
                moves.append(Move(x, y, x + 1, y + 1))
            # kill diagonally
            if self.is_valid(x - 1, y + 1) \
                    and b.get_tile(x - 1, y + 1).is_occupied() \
                    and b.get_tile(x - 1, y + 1).get_piece().get_color() != self.color:
                moves.append(Move(x, y, x - 1, y + 1))
        else:
            # forward
            if self.is_valid(x, y - 1) \
                    and not b.get_tile(x, y - 1).is_occupied():
                moves.append(Move(x, y, x, y - 1))
            # kill diagonally
            if self.is_valid(x + 1, y - 1) \
                    and b.get_tile(x + 1, y - 1).is_occupied() \
                    and b.get_tile(x + 1, y - 1).get_piece().get_color() != self.color:
                moves.append(Move(x, y, x + 1, y - 1))
            # kill diagonally
            if self.is_valid(x - 1, y - 1) \
                    and b.get_tile(x - 1, y - 1).is_occupied() \
                    and b.get_tile(x - 1, y - 1).get_piece().get_color() != self.color:
                moves.append(Move(x, y, x - 1, y - 1))

        return moves
