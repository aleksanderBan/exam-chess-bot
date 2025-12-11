import chess
import numpy as np
from .opening import play_opening
from .minimax import minimax

def get_move(board, depth):
    opening_move = play_opening(board)
    if opening_move:
        print("PLAYING OPENING MOVE:", opening_move)
        return opening_move

    best_move = None
    maximizing = board.turn
    best_eval = -np.inf if maximizing else np.inf

    for move in board.legal_moves:
        board.push(move)
        val = minimax(board, depth - 1, -np.inf, np.inf, not maximizing)
        board.pop()

        if maximizing and val > best_eval:
            best_eval, best_move = val, move
        elif not maximizing and val < best_eval:
            best_eval, best_move = val, move

    print("CHOSEN MOVE:", best_move, "WITH EVAL:", best_eval)
    return best_move
