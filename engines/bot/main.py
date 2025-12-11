import chess
import numpy as np
from .opening import play_opening
from .minimax import minimax

def get_move(board, depth):
    opening_move = play_opening(board)
    if opening_move:
        print("PLAYING OPENING MOVE:", opening_move)
        return opening_move

    top_move = None
    
    maximizing = board.turn
    if maximizing:
      top_eval = -np.inf
    else:
      top_eval = np.inf

    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, -np.inf, np.inf, not maximizing)
        board.pop()

        if maximizing and eval > top_eval:
            top_move = move
            top_eval = eval
        elif not maximizing and eval < top_eval:
            top_move = move
            top_eval = eval

    print("CHOSEN MOVE:", top_move, "WITH EVAL:", top_eval)
    return top_move
