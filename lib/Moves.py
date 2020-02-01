def trailing_zeros(s):
    return len(s) - len(s.rstrip("0"))


class Moves(object):
    def __init__(self, board):
        self.utilities = {
            "file_a": 72340172838076673,
            "file_h": 9259542123273814144,
            "file_ab": 217020518514230019,
            "file_gh": 13889313184910721216,
            "rank_1": 18374686479671623680,
            "rank_4": 1095216660480,
            "rank_5": 4278190080,
            "rank_8": 255,
            "centre": 103481868288,
            "extended_centre": 66229406269440,
            "king_side": 17361641481138401520,
            "queen_side": 1085102592571150095,
            "king_b7": 460039,
            "knight_c6": 43234889994,
            "not_white_pieces": ~(board.pieces["WR"] | board.pieces["WN"] | board.pieces["WB"] |
                board.pieces["WQ"] | board.pieces["WK"] | board.pieces["WP"] | board.pieces["BK"]),
            "black_pieces": (board.pieces["BR"] | board.pieces["BN"] |
                board.pieces["BB"] | board.pieces["BQ"] | board.pieces["BP"]),
            "empty": ~(board.pieces["WR"] | board.pieces["WN"] | board.pieces["WB"] | 
                board.pieces["WQ"] | board.pieces["WK"] | board.pieces["WP"] | 
                board.pieces["BR"] | board.pieces["BN"] | board.pieces["BB"] |
                board.pieces["BQ"] | board.pieces["BK"] | board.pieces["BP"])
        }

    def white_pawn_moves(self, pawn):
        moves_list = ""
        all = self.utilities
        # Common movement, x1x2y1y2
        pawn_moves = (pawn >> 7) & all["black_pieces"] & ~all["rank_8"] & ~all["file_a"] # Capture right
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i//8 + 1) + str(i%8 - 1) + str(i//8) + str(i%8)
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 9) & all["black_pieces"] & ~all["rank_8"] & ~all["file_h"] # Capture left
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i//8 + 1) + str(i%8 + 1) + str(i//8) + str(i%8)
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 8) & all["empty"] & ~all["rank_8"] # Simple move
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i//8 + 1) + str(i%8) + str(i//8) + str(i%8)
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 16) & all["empty"] & ~all["rank_8"] & all["rank_4"] # Double move
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i//8 + 2) + str(i%8) + str(i//8) + str(i%8)
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        # Promotion y1y2
        pawn_moves = (pawn >> 7) & all["black_pieces"] & all["rank_8"] & ~all["file_a"] # Capture right and promotion
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i%8 - 1) + str(i%8) + "QP" +vstr(i%8 - 1) + str(i%8) 
            + "RP" + str(i%8 - 1) + str(i%8) + "NP" + str(i%8 - 1) + str(i%8) + "BP"
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 9) & all["black_pieces"] & all["rank_8"] & ~all["file_h"] # Capture left and promotion
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i%8 + 1) + str(i%8) + "QP" + str(i%8 + 1) + str(i%8) 
            + "RP" + str(i%8 + 1) + str(i%8) + "NP" + str(i%8 + 1) + str(i%8) + "BP"
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 8) & all["empty"] & all["rank_8"] # Simple move and promotion
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i%8) + str(i%8) + "QP" + str(i%8) + str(i%8) 
            + "RP" + str(i%8) + str(i%8) + "NP" + str(i%8) + str(i%8) + "BP"
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        return moves_list
