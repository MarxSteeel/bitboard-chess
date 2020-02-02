from lib.BoardGeneration import BoardGeneration
from lib.Moves import Moves

board = BoardGeneration()
pieces = board.pieces
# print(pieces)
# print(bin(pieces["WR"]))
print(board.chessBoard)
print(board.pieces)
print(board.drawArray())
moves = Moves(board)
history = [["BN", "0120"], ["BP", "1636"]]
# print(moves.utilities)
print(moves.white_pawn_moves(pieces["WP"], history))
