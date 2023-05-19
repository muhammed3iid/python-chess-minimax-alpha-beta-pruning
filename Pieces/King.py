from abc import abstractmethod

from Move import Move
from Pieces.Piece import Piece
from Pieces.Rook import Rook


class King(Piece):

    def __init__(self, *args):
        super().__init__(args[0])
        self.value = 0
        if len(args) == 1:
            self.has_moved = False
        else:
            self.has_moved = args[1]

    def __str__(self):
        if self.color == Piece.WHITE:
            return '\u2654'
        else:
            return '\u265A'

    def clone(self):
        return King(self.color, self.has_moved)

    def get_moves(self, board, x, y):
        moves = []
        self.traverse_north(board, x, y, moves)
        self.traverse_north_east(board, x, y, moves)
        self.traverse_east(board, x, y, moves)
        self.traverse_south_east(board, x, y, moves)
        self.traverse_south(board, x, y, moves)
        self.traverse_south_west(board, x, y, moves)
        self.traverse_west(board, x, y, moves)
        self.traverse_north_west(board, x, y, moves)
        self.castling(board, x, y, moves)
        return moves

    def traverse_north(self, board, x, y, moves):
        if self.is_valid(x, y + 1) and \
                (not board.get_tile(x, y + 1).is_occupied() or
                 (board.get_tile(x, y + 1).is_occupied() and
                  board.get_tile(x, y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x, y + 1))

    def traverse_north_east(self, board, x, y, moves):
        if self.is_valid(x + 1, y + 1) and \
                (not board.get_tile(x + 1, y + 1).is_occupied() or
                 (board.get_tile(x + 1, y + 1).is_occupied() and
                  board.get_tile(x + 1, y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y + 1))

    def traverse_east(self, board, x, y, moves):
        if self.is_valid(x + 1, y) and \
                (not board.get_tile(x + 1, y).is_occupied() or
                 (board.get_tile(x + 1, y).is_occupied() and
                  board.get_tile(x + 1, y).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y))

    def traverse_south_east(self, board, x, y, moves):
        if self.is_valid(x + 1, y - 1) and \
                (not board.get_tile(x + 1, y - 1).is_occupied() or
                 (board.get_tile(x + 1, y - 1).is_occupied() and
                  board.get_tile(x + 1, y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y - 1))

    def traverse_south(self, board, x, y, moves):
        if self.is_valid(x, y - 1) and \
                (not board.get_tile(x, y - 1).is_occupied() or
                 (board.get_tile(x, y - 1).is_occupied() and
                  board.get_tile(x, y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x, y - 1))

    def traverse_south_west(self, board, x, y, moves):
        if self.is_valid(x - 1, y - 1) and \
                (not board.get_tile(x - 1, y - 1).is_occupied() or
                 (board.get_tile(x - 1, y - 1).is_occupied() and
                  board.get_tile(x - 1, y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y - 1))

    def traverse_west(self, board, x, y, moves):
        if self.is_valid(x - 1, y) and \
                (not board.get_tile(x - 1, y).is_occupied() or
                 (board.get_tile(x - 1, y).is_occupied() and
                     board.get_tile(x - 1, y).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y))

    def traverse_north_west(self, board, x, y, moves):
        if self.is_valid(x - 1, y + 1) and \
                ((not board.get_tile(x - 1, y + 1).is_occupied()) or
                 (board.get_tile(x - 1, y + 1).is_occupied() and
                     board.get_tile(x - 1, y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y + 1))

    def castling(self, board, x, y, moves):
        if self.color == Piece.WHITE:
            if not self.has_moved and x == board.e and y == 1 - 1:
                if not board.get_tile(board.f, 1 - 1).is_occupied() and \
                        not board.get_tile(board.g, 1 - 1).is_occupied() and \
                        board.get_tile(board.h, 1 - 1).is_occupied() and \
                        isinstance(board.get_tile(board.h, 1 - 1).get_piece(), Rook):
                    moves.append(Move(x, y, x + 2, y))
            else:
                self.has_moved = True
        else:
            if not self.has_moved and x == board.e and y == 8 - 1:
                if not board.get_tile(board.f, 8 - 1).is_occupied() and \
                        not board.get_tile(board.g, 8 - 1).is_occupied() and \
                        board.get_tile(board.h, 8 - 1).is_occupied() and \
                        isinstance(board.get_tile(board.h, 8 - 1).get_piece(), Rook):
                    moves.append(Move(x, y, x + 2, y))
            else:
                self.has_moved = True
