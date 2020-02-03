from lib.BoardGeneration import BoardGeneration
from lib.Moves import Moves

board = BoardGeneration()
pieces = board.pieces
# print(pieces)
# print(bin(pieces["WR"]))
# print(board.chessBoard)
# print(board.pieces)
# print(board.drawArray())
moves = Moves(board)
history = [["BN", "0120"], ["BP", "1636"]]
# print(len(bin(moves.utilities["rank_masks"][4])))
# print(moves.utilities)
print(moves.white_pawn_moves(pieces["WP"], history))
# print(moves.hv_moves(35))  # Por algun motivo no funciona con numeros < 8
# print(moves.diag_moves(35))
# print(moves.white_bishop_moves(pieces["WB"]))
# print(moves.white_rook_moves(pieces["WR"]))
# print(moves.white_queen_moves(pieces["WQ"]))
