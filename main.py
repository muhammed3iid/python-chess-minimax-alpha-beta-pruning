from Board import Board
from Pieces.Piece import Piece
from Players.MinimaxPlayer import MinimaxPlayer
from Players.RandomPlayer import RandomPlayer


def main():
    player1_score = 0
    draw = 0
    board = Board()
    player1 = MinimaxPlayer(Piece.WHITE, 4)
    player2 = RandomPlayer(Piece.BLACK)
    winner = play(player1, player2, board)
    if winner == 1:
        player1_score += 1
    elif winner == 0:
        player1_score += 0.5
        draw += 1
    print(player1_score)


def play(player1, player2, board):
    turn = 0
    while True:
        turn += 1
        if turn > 200:
            return 0
        move = player1.get_next_move(board)
        if move is None and board.is_check(player1.get_color()):
            return -1
        if move is None:
            return 0
        board.make_move(move)
        print(board)
        move = player2.get_next_move(board)
        if move is None and board.is_check(player2.get_color()):
            return 1
        if move is None:
            return 0
        board.make_move(move)
        print(board)


if __name__ == "__main__":
    main()
