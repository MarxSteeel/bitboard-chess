from lib.BoardGeneration import BoardGeneration
from lib.Moves import Moves

board = BoardGeneration()
pieces = board.pieces
# print(pieces)
# print(bin(pieces["WR"]))
# print(board.drawArray())
moves = Moves(board)
# print(moves.utilities)
print(moves.white_pawn_moves(pieces["WP"]))
