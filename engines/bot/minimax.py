from .evaluation import get_evaluation
import numpy as np
import chess

def order_moves(board):
    captures = []
    checks = []
    others = []
    for move in board.legal_moves:
        if board.is_capture(move):
            captures.append(move)
        elif board.gives_check(move):
            checks.append(move)
        else:
            others.append(move)
    return captures + checks + others

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return get_evaluation(board)

    moves = order_moves(board)

    if maximizing_player:
        max_eval = -np.inf
        for move in moves:
            board.push(move)
            val = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = np.inf
        for move in moves:
            board.push(move)
            val = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return min_eval
