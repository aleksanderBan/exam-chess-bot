from .material import get_material
from . import positions
import chess

PIECE_TABLES = {
    chess.PAWN: positions.pawn,
    chess.KNIGHT: positions.knight,
    chess.BISHOP: positions.bishop,
    chess.ROOK: positions.rook,
    chess.QUEEN: positions.queen,
    chess.KING: positions.king,
}

def get_evaluation(board):
    if board.is_checkmate():
        return -9999 if board.turn else 9999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    eval = get_material(board)

    for piece_type, table in PIECE_TABLES.items():
        for sq in board.pieces(piece_type, chess.WHITE):
            eval += table[sq]
        for sq in board.pieces(piece_type, chess.BLACK):
            eval -= table[chess.square_mirror(sq)]

    return eval
