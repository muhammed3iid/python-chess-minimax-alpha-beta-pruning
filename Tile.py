from Pieces.Piece import Piece


class Tile:

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], Tile):
                self.occupied = args[0].is_occupied()
                self.piece = args[0].get_piece().clone() if args[0].is_occupied() else None
            elif isinstance(args[0], Piece):
                self.occupied = True
                self.piece = args[0]
        else:
            self.occupied = False
            self.piece = None

    # def __init__(self, tile):
    #     self.occupied = tile.is_occupied()
    #     self.piece = tile.get_piece().clone() if tile.is_occupied() else None
    #
    # def __init__(self, piece):
    #     self.occupied = True
    #     self.piece = piece

    def __str__(self):
        if self.occupied:
            return str(self.piece)
        else:
            return "."

    def is_occupied(self):
        return self.occupied

    def get_piece(self):
        return self.piece
