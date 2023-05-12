from typing import List

from Move import Move
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Piece import Piece
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Tile import Tile


class Board:
    a, b, c, d, e, f, g, h = range(8)

    def __init__(self, *args):
        if len(args) == 1:
            self.tiles = args[0]
        else:
            color = Piece.WHITE
            self.tiles = [[Tile() for j in range(8)] for i in range(8)]
            self.tiles[Board.a][1 - 1] = Tile(Rook(color))
            self.tiles[Board.b][1 - 1] = Tile(Knight(color))
            self.tiles[Board.c][1 - 1] = Tile(Bishop(color))
            self.tiles[Board.d][1 - 1] = Tile(Queen(color))
            self.tiles[Board.e][1 - 1] = Tile(King(color))
            self.tiles[Board.f][1 - 1] = Tile(Bishop(color))
            self.tiles[Board.g][1 - 1] = Tile(Knight(color))
            self.tiles[Board.h][1 - 1] = Tile(Rook(color))
            for i in range(8):
                self.tiles[i][2 - 1] = Tile(Pawn(color))
            for i in range(2, 7):
                for j in range(8):
                    self.tiles[j][i] = Tile()
            color = Piece.BLACK
            self.tiles[Board.a][8 - 1] = Tile(Rook(color))
            self.tiles[Board.b][8 - 1] = Tile(Knight(color))
            self.tiles[Board.c][8 - 1] = Tile(Bishop(color))
            self.tiles[Board.d][8 - 1] = Tile(Queen(color))
            self.tiles[Board.e][8 - 1] = Tile(King(color))
            self.tiles[Board.f][8 - 1] = Tile(Bishop(color))
            self.tiles[Board.g][8 - 1] = Tile(Knight(color))
            self.tiles[Board.h][8 - 1] = Tile(Rook(color))
            for i in range(8):
                self.tiles[i][7 - 1] = Tile(Pawn(color))

    def __str__(self):
        acc_string = ""
        for i in range(7, -1, -1):
            acc_string += f"{i + 1}  "
            for j in range(8):
                acc_string += f"{self.tiles[j][i]} "
            acc_string += "\n"
        acc_string += "\n   a b c d e f g h"
        return acc_string

    def get_moves(self, color):
        return self.get_moves_with_check(color, True)

    def get_moves_with_check(self, color, check):
        moves = []
        for i in range(8):
            for j in range(8):
                if self.tiles[i][j].is_occupied() and self.tiles[i][j].get_piece().get_color() == color:
                    moves.extend(self.tiles[i][j].get_piece().get_moves(self, i, j))
        # check if move is valid (must not be checked after move) and throw away erroneous moves
        if check:
            # find king (of correct color)
            x, y = -1, -1
            for i in range(8):
                for j in range(8):
                    if self.tiles[i][j].is_occupied() and self.tiles[i][j].get_piece().get_color() == color and \
                            str(self.tiles[i][j].get_piece()).lower() == 'k':
                        x, y = i, j
            remove_these = []
            for i in range(len(moves)):
                if i >= len(moves):
                    continue
                # check a move if after making this move the king can be killed (moving into check)
                check_this = moves[i:i+1]
                opponent_moves = self.get_moves_after_with_check(not color, check_this, False)
                x_updated, y_updated = x, y
                if check_this[0].get_x1() == x and check_this[0].get_y1() == y:
                    # get updated king position
                    x_updated, y_updated = check_this[0].get_x2(), check_this[0].get_y2()
                # check all opponent moves if they kill king (opponent moves in next round)
                for j in range(len(opponent_moves)):
                    if opponent_moves[j].get_x2() == x_updated and opponent_moves[j].get_y2() == y_updated:
                        remove_these.append(check_this[0])
                        # if check_this[0] in moves:
                        #     moves.remove(check_this[0])
            # for move in remove_these:
                # moves.remove(move)  # remove invalid moves
            moves = [move for move in moves if move not in remove_these]
        return moves

    def is_check(self, color):
        x, y = -1, -1
        for i in range(8):
            for j in range(8):
                if (self.tiles[i][j].is_occupied() and
                        self.tiles[i][j].get_piece().get_color() == color and
                        str(self.tiles[i][j].get_piece()).lower() == "k"):
                    x, y = i, j
        # check a move if after making this move the king can be killed (moving into check)
        opponent_moves = self.get_moves_with_check(not color, False)
        # check all opponent moves if they kill king (opponent moves in next round)
        for move in range(len(opponent_moves)):
            if opponent_moves[move].get_x2() == x and opponent_moves[move].get_y2() == y:
                return True
        return False

    def is_check_after(self, color, moves):
        new_tiles = self.get_tiles_after(moves)
        x, y = -1, -1
        for i in range(8):
            for j in range(8):
                if (new_tiles[i][j].is_occupied() and
                        new_tiles[i][j].get_piece().get_color() == color and
                        str(new_tiles[i][j].get_piece()).lower() == "k"):
                    x, y = i, j
        # check a move if after making this move the king can be killed (moving into check)
        opponent_moves = self.get_moves_after_with_check(not color, moves, False)
        # check all opponent moves if they kill king (opponent moves in next round)
        for move in opponent_moves:
            if move.get_x2() == x and move.get_y2() == y:
                return True
        return False

    def get_moves_after_with_check(self, color, moves, check):
        temp = [[Tile(t) for t in row] for row in self.tiles]
        b = Board(temp)
        for move in moves:
            b.make_move(move)
        future_moves = b.get_moves_with_check(color, check)
        return future_moves

    def get_moves_after(self, color, moves):
        return self.get_moves_after_with_check(color, moves, True)

    def get_tiles_after(self, moves):
        temp = [[Tile(t) for t in row] for row in self.tiles]
        b = Board(temp)
        for move in moves:
            b.make_move(move)
        temp2 = [[Tile(b.get_tile(x, y)) for y in range(8)] for x in range(8)]
        return temp2

    def make_move(self, move):
        old_tile = self.tiles[move.get_x1()][move.get_y1()]
        self.tiles[move.get_x2()][move.get_y2()] = self.tiles[move.get_x1()][move.get_y1()]
        self.tiles[move.get_x1()][move.get_y1()] = Tile()
        if move.is_castling():
            if move.get_x2() == self.g and move.get_y2() == 1 - 1:
                self.tiles[self.f][1 - 1] = self.tiles[self.h][1 - 1]
                self.tiles[self.h][1 - 1] = Tile()
            if move.get_x2() == self.c and move.get_y2() == 1 - 1:
                self.tiles[self.d][1 - 1] = self.tiles[self.a][1 - 1]
                self.tiles[self.a][1 - 1] = Tile()
            if move.get_x2() == self.g and move.get_y2() == 8 - 1:
                self.tiles[self.f][8 - 1] = self.tiles[self.h][8 - 1]
                self.tiles[self.h][8 - 1] = Tile()
            if move.get_x2() == self.c and move.get_y2() == 8 - 1:
                self.tiles[self.d][8 - 1] = self.tiles[self.a][8 - 1]
                self.tiles[self.a][8 - 1] = Tile()
        # pawn at top?
        if str(old_tile.get_piece()) == "P" and move.get_y2() == 8 - 1:
            self.tiles[move.get_x2()][move.get_y2()] = Tile(Queen(Piece.WHITE))
        if str(old_tile.get_piece()) == "p" and move.get_y2() == 1 - 1:
            self.tiles[move.get_x2()][move.get_y2()] = Tile(Queen(Piece.BLACK))
        return 0

    def get_tile(self, x, y):
        return self.tiles[x][y]