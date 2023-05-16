import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from concurrent import futures
from Pieces.Piece import Piece


class Minimax:

    def __init__(self, color, max_depth):
        self.color = color
        self.max_depth = max_depth
        self.rand = random.Random()

    def max_value(self, board, state, alpha, beta, depth):
        if depth > self.max_depth:
            return self.eval1(board, state, self.color)
        moves = board.get_moves_after(self.color, state)
        if len(moves) == 0:
            return float('-inf')
        for i in range(len(moves)):
            state.append(moves[i])
            tmp = self.min_value(board, state, alpha, beta, depth + 1)
            state.remove(state[state[::-1].index(moves[i])])
            if tmp > alpha:
                alpha = tmp
            if beta <= alpha:
                break
        return alpha

    def min_value(self, board, state, alpha, beta, depth):
        if depth > self.max_depth:
            return self.eval1(board, state, not self.color)
        moves = board.get_moves_after(not self.color, state)
        if len(moves) == 0:
            return float('inf')
        for i in range(len(moves)):
            state.append(moves[i])
            tmp = self.max_value(board, state, alpha, beta, depth + 1)
            state.remove(state[state[::-1].index(moves[i])])
            if tmp < beta:
                beta = tmp
            if beta <= alpha:
                break
        return beta

    def decision(self, board):
        moves = board.get_moves(self.color)
        if len(moves) == 0:
            return None
        costs = []

        with ProcessPoolExecutor(max_workers=len(moves)) as executor:
            futures = []
            for move in moves:
                state = [move]
                future = executor.submit(self.min_value, board, state, float('-inf'), float('inf'), 1)
                costs.append(future)
        for i, future in enumerate(as_completed(futures)):
            costs[i] = future.result()
        maxi = -1
        max_cost = float('-inf')
        for i, cost in enumerate(costs):
            try:
                cost = cost.result()
            except Exception:
                # time.sleep(0.3)
                continue
            if cost >= max_cost:
                if abs(cost - max_cost) < 0.1:
                    if random.random() < 0.5:
                        continue
                max_cost = cost
                maxi = i
        return moves[maxi]


    def single_thread_decision(self, b):
        # get maximum move
        moves = b.get_moves(self.color)
        state = []
        costs = []
        for move in moves:
            state.append(move)
            cost = self.min_value(b, state, float('-inf'), float('inf'), 1)
            costs.append(cost)
            state.remove(state[-1])
        # max
        maxi = -1
        max_cost = float('-inf')
        for i, cost in enumerate(costs):
            if cost >= max_cost:
                if abs(cost - max_cost) < 0.1:
                    if random.choice([True, False]):
                        continue
                max_cost = cost
                maxi = i
        if maxi == -1:
            return None
        else:
            return moves[maxi]

    def eval1(self, b, moves, current_color):
        tiles = b.get_tiles_after(moves)
        if len(b.get_moves(current_color)) == 0:
            if b.is_check_after(current_color, moves):
                if current_color == self.color:
                    return float('-inf')
                else:
                    float('inf')
            else:
                return float('-inf')
        white_score, black_score = 0, 0
        for i in range(8):
            for j in range(8):
                if tiles[i][j].is_occupied():
                    if tiles[i][j].get_piece().get_color() == Piece.WHITE:
                        white_score += tiles[i][j].get_piece().get_value()
                    else:
                        black_score += tiles[i][j].get_piece().get_value()
        if self.color == Piece.WHITE:
            return white_score - black_score
        else:
            return black_score - white_score

    def eval2(self, b, moves, current_color):
        tiles = b.get_tiles_after(moves)
        black_king, white_king = False, False
        for i in range(8):
            for j in range(8):
                if tiles[i][j].is_occupied():
                    if tiles[i][j].get_piece().get_value() == 0 and tiles[i][j].get_piece().get_color() == Piece.WHITE:
                        white_king = True
                    if tiles[i][j].get_piece().get_value() == 0 and tiles[i][j].get_piece().get_color() != Piece.WHITE:
                        black_king = True
        if self.color == Piece.WHITE:
            if not white_king:
                return float('-inf')
            if not black_king:
                return float('inf')
        else:
            if not white_king:
                return float('inf')
            if not black_king:
                return float('-inf')
        white_score, black_score = 0, 0
        for i in range(8):
            for j in range(8):
                if tiles[i][j].is_occupied():
                    if tiles[i][j].get_piece().get_color == Piece.WHITE:
                        white_score += tiles[i][j].get_piece().get_value()
                    else:
                        black_score += tiles[i][j].get_piece().get_value()
        if self.color == Piece.WHITE:
            return white_score - black_score
        else:
            return black_score - white_score
