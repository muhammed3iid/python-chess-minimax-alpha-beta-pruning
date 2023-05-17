class Move:

    def __init__(self, *args):
        self.x1 = args[0]
        self.y1 = args[1]
        self.x2 = args[2]
        self.y2 = args[3]
        if len(args) == 4:
            self.castling = False
        else:
            self.castling = args[4]



    def __str__(self):
        return chr(ord('A') + self.x1) + str(self.y1 + 1) + " " + chr(ord('A') + self.x2) + str(self.y2 + 1)

    def __eq__(self, other):
        if not isinstance(other, Move):
            return False
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2

    def get_x1(self):
        return self.x1

    def set_x1(self, x1):
        self.x1 = x1

    def get_x2(self):
        return self.x2

    def set_x2(self, x2):
        self.x2 = x2

    def get_y1(self):
        return self.y1

    def set_y1(self, y1):
        self.y1 = y1

    def get_y2(self):
        return self.y2

    def set_y2(self, y2):
        self.y2 = y2

    def is_castling(self):
        return self.castling
