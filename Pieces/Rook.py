from Move import Move
from Pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.value = 5

    def __str__(self):
        if self.color == Piece.WHITE:
            return "R"
        else:
            return "r"

    def clone(self):
        return Rook(self.color)

    def get_moves(self, b, x, y):
        moves = []
        # up
        for i in range(1, 8):
            if self.is_valid(x, y + i):
                if b.get_tile(x, y + i).is_occupied():
                    if b.get_tile(x, y + i).get_piece().color != self.color:
                        moves.append(Move(x, y, x, y + i))
                    break
                else:
                    moves.append(Move(x, y, x, y + i))
        # down
        for i in range(1, 8):
            if self.is_valid(x, y - i):
                if b.get_tile(x, y - i).is_occupied():
                    if b.get_tile(x, y - i).get_piece().color != self.color:
                        moves.append(Move(x, y, x, y - i))
                    break
                else:
                    moves.append(Move(x, y, x, y - i))
        # left
        for i in range(1, 8):
            if self.is_valid(x - i, y):
                if b.get_tile(x - i, y).is_occupied():
                    if b.get_tile(x - i, y).get_piece().color != self.color:
                        moves.append(Move(x, y, x - i, y))
                    break
                else:
                    moves.append(Move(x, y, x - i, y))
        # right
        for i in range(1, 8):
            if self.is_valid(x + i, y):
                if b.get_tile(x + i, y).is_occupied():
                    if b.get_tile(x + i, y).get_piece().color != self.color:
                        moves.append(Move(x, y, x + i, y))
                    break
                else:
                    moves.append(Move(x, y, x + i, y))
        return moves
