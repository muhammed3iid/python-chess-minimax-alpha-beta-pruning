from Move import Move
from Pieces.Piece import Piece


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.value = 3

    def __str__(self):
        if self.color == Piece.WHITE:
            return '\u2657'
        else:
            return '\u265D'

    def clone(self):
        return Bishop(self.color)

    def get_moves(self, board, x, y):
        moves = []
        self.traverse_south_west(board, x, y, moves)
        self.traverse_north_east(board, x, y, moves)
        self.traverse_south_east(board, x, y, moves)
        self.traverse_north_west(board, x, y, moves)
        return moves

    def traverse_north_east(self, board, x, y, moves):
        for i in range(1, 8):
            if self.is_valid(x + i, y + i):
                if board.get_tile(x + i, y + i).is_occupied():
                    if board.get_tile(x + i, y + i).get_piece().color != self.color:
                        moves.append(Move(x, y, x + i, y + i))
                    break
                else:
                    moves.append(Move(x, y, x + i, y + i))

    def traverse_north_west(self, board, x, y, moves):
        for i in range(1, 8):
            if self.is_valid(x - i, y + i):
                if board.get_tile(x - i, y + i).is_occupied():
                    if board.get_tile(x - i, y + i).get_piece().color != self.color:
                        moves.append(Move(x, y, x - i, y + i))
                    break
                else:
                    moves.append(Move(x, y, x - i, y + i))

    def traverse_south_east(self, board, x, y, moves):
        for i in range(1, 8):
            if self.is_valid(x + i, y - i):
                if board.get_tile(x + i, y - i).is_occupied():
                    if board.get_tile(x + i, y - i).get_piece().color != self.color:
                        moves.append(Move(x, y, x + i, y - i))
                    break
                else:
                    moves.append(Move(x, y, x + i, y - i))

    def traverse_south_west(self, board, x, y, moves):
        for i in range(1, 8):
            if self.is_valid(x - i, y - i):
                if board.get_tile(x - i, y - i).is_occupied():
                    if board.get_tile(x - i, y - i).get_piece().color != self.color:
                        moves.append(Move(x, y, x - i, y - i))
                    break
                else:
                    moves.append(Move(x, y, x - i, y - i))
