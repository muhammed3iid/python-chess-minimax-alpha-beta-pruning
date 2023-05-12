from Move import Move
from Pieces.Piece import Piece


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.value = 8

    def __str__(self):
        if self.color == Piece.WHITE:
            return "Q"
        else:
            return "q"

    def clone(self):
        return Queen(self.color)

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
        # NE
        for i in range(1, 8):
            if self.is_valid(x + i, y + i):
                if b.get_tile(x + i, y + i).is_occupied():
                    if b.get_tile(x + i, y + i).get_piece().color != self.color:
                        moves.append(Move(x, y, x + i, y + i))
                    break
                else:
                    moves.append(Move(x, y, x + i, y + i))
        # NW
        for i in range(1, 8):
            if self.is_valid(x - i, y + i):
                if b.get_tile(x - i, y + i).is_occupied():
                    if b.get_tile(x - i, y + i).get_piece().color != self.color:
                        moves.append(Move(x, y, x - i, y + i))
                    break
                else:
                    moves.append(Move(x, y, x - i, y + i))
        # SE
        for i in range(1, 8):
            if self.is_valid(x + i, y - i):
                if b.get_tile(x + i, y - i).is_occupied():
                    if b.get_tile(x + i, y - i).get_piece().color != self.color:
                        moves.append(Move(x, y, x + i, y - i))
                    break
                else:
                    moves.append(Move(x, y, x + i, y - i))
        # SW
        for i in range(1, 8):
            if self.is_valid(x - i, y - i):
                if b.get_tile(x - i, y - i).is_occupied():
                    if b.get_tile(x - i, y - i).get_piece().color != self.color:
                        moves.append(Move(x, y, x - i, y - i))
                    break
                else:
                    moves.append(Move(x, y, x - i, y - i))
        return moves
