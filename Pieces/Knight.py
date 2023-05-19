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
        self.traverse_north_north_east(board, x, y, moves)
        self.traverse_east_north_east(board, x, y, moves)
        self.traverse_east_south_east(board, x, y, moves)
        self.traverse_south_south_east(board, x, y, moves)
        self.traverse_south_south_west(board, x, y, moves)
        self.traverse_west_south_west(board, x, y, moves)
        self.traverse_west_north_west(board, x, y, moves)
        self.traverse_north_north_west(board, x, y, moves)
        return moves

    def traverse_north_north_east(self, board, x, y, moves):
        if self.is_valid(x + 1, y + 2) and \
                (not board.get_tile(x + 1, y + 2).is_occupied() or
                 (board.get_tile(x + 1, y + 2).is_occupied() and
                  board.get_tile(x + 1, y + 2).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y + 2))

    def traverse_east_north_east(self, board, x, y, moves):
        if self.is_valid(x + 2, y + 1) and \
                (not board.get_tile(x + 2, y + 1).is_occupied() or
                 (board.get_tile(x + 2, y + 1).is_occupied() and
                  board.get_tile(x + 2, y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 2, y + 1))

    def traverse_east_south_east(self, board, x, y, moves):
        if self.is_valid(x + 2, y - 1) and \
                (not board.get_tile(x + 2, y - 1).is_occupied() or
                 (board.get_tile(x + 2, y - 1).is_occupied() and
                  board.get_tile(x + 2, y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 2, y - 1))

    def traverse_south_south_east(self, board, x, y, moves):
        if self.is_valid(x + 1, y - 2) and \
                (not board.get_tile(x + 1, y - 2).is_occupied() or
                 (board.get_tile(x + 1, y - 2).is_occupied() and
                  board.get_tile(x + 1, y - 2).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y - 2))

    def traverse_south_south_west(self, board, x, y, moves):
        if self.is_valid(x - 1, y - 2) and \
                (not board.get_tile(x - 1, y - 2).is_occupied() or
                 (board.get_tile(x - 1, y - 2).is_occupied() and
                  board.get_tile(x - 1, y - 2).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y - 2))

    def traverse_west_south_west(self, board, x, y, moves):
        if self.is_valid(x - 2, y - 1) and \
                (not board.get_tile(x - 2, y - 1).is_occupied() or
                 (board.get_tile(x - 2, y - 1).is_occupied() and
                  board.get_tile(x - 2, y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 2, y - 1))

    def traverse_west_north_west(self, board, x, y, moves):
        if self.is_valid(x - 2, y + 1) and \
                (not board.get_tile(x - 2, y + 1).is_occupied() or
                 (board.get_tile(x - 2, y + 1).is_occupied() and
                  board.get_tile(x - 2, y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 2, y + 1))

    def traverse_north_north_west(self, board, x, y, moves):
        if self.is_valid(x - 1, y + 2) and \
                (not board.get_tile(x - 1, y + 2).is_occupied() or
                 (board.get_tile(x - 1, y + 2).is_occupied() and
                  board.get_tile(x - 1, y + 2).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y + 2))
