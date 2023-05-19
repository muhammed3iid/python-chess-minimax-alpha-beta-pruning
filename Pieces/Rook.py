from Move import Move
from Pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.value = 5

    def __str__(self):
        if self.color == Piece.WHITE:
            return '\u2656'
        else:
            return '\u265C'

    def clone(self):
        return Rook(self.color)

    def get_moves(self, board, x, y):
        moves = []
        self.traverse_north(board, x, y, moves),
        self.traverse_south(board, x, y, moves),
        self.traverse_west(board, x, y, moves),
        self.traverse_east(board, x, y, moves)
        return moves

    def traverse_north(self, board, x, y, moves):
        for i in range(1, 8):
            if self.is_valid(x, y + i):
                if board.get_tile(x, y + i).is_occupied():
                    if board.get_tile(x, y + i).get_piece().color != self.color:
                        moves.append(Move(x, y, x, y + i))
                    break
                else:
                    moves.append(Move(x, y, x, y + i))

    def traverse_south(self, board, x, y, moves):
        for i in range(1, 8):
            if self.is_valid(x, y - i):
                if board.get_tile(x, y - i).is_occupied():
                    if board.get_tile(x, y - i).get_piece().color != self.color:
                        moves.append(Move(x, y, x, y - i))
                    break
                else:
                    moves.append(Move(x, y, x, y - i))

    def traverse_west(self, board, x, y, moves):
        for i in range(1, 8):
            if self.is_valid(x - i, y):
                if board.get_tile(x - i, y).is_occupied():
                    if board.get_tile(x - i, y).get_piece().color != self.color:
                        moves.append(Move(x, y, x - i, y))
                    break
                else:
                    moves.append(Move(x, y, x - i, y))

    def traverse_east(self, board, x, y, moves):
        for i in range(1, 8):
            if self.is_valid(x + i, y):
                if board.get_tile(x + i, y).is_occupied():
                    if board.get_tile(x + i, y).get_piece().color != self.color:
                        moves.append(Move(x, y, x + i, y))
                    break
                else:
                    moves.append(Move(x, y, x + i, y))
