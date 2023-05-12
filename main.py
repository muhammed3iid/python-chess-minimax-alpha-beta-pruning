from Board import Board
from Pieces.Piece import Piece
from Players.RandomPlayer import RandomPlayer


def main():
    player1_score = 0
    draw = 0
    board = Board()
    player1 = RandomPlayer(Piece.WHITE)
    player2 = RandomPlayer(Piece.BLACK)
    winner = play(player1, player2, board)
    if winner == 1:
        player1_score += 1
    elif winner == 0:
        player1_score += 0.5
        draw += 1
    print(player1_score)


def play(player1, player2, b):
    print(b)
    turn = 0
    while True:
        turn += 1
        if turn > 200:
            return 0
        move = player1.get_next_move(b)
        if move is None and b.is_check(player1.get_color()):  # check and can't move
            return -1
        if move is None:  # no check but can't move
            return 0
        result = b.make_move(move)
        print(b)
        move = player2.get_next_move(b)
        if move is None and b.is_check(player2.get_color()):
            return 1
        if move is None:  # no check but can't move
            return 0
        result = b.make_move(move)
        print(b)

if __name__ == "__main__":
    main()
