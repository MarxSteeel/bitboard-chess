def trailing_zeros(s):
    return len(s) - len(s.rstrip("0"))


def reverse(n):
    return int('{:064b}'.format(n)[::-1], 2)


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
            "occupied": (board.pieces["WR"] | board.pieces["WN"] | board.pieces["WB"] | 
                board.pieces["WQ"] | board.pieces["WK"] | board.pieces["WP"] | 
                board.pieces["BR"] | board.pieces["BN"] | board.pieces["BB"] |
                board.pieces["BQ"] | board.pieces["BK"] | board.pieces["BP"]),
            "empty": ~(board.pieces["WR"] | board.pieces["WN"] | board.pieces["WB"] | 
                board.pieces["WQ"] | board.pieces["WK"] | board.pieces["WP"] | 
                board.pieces["BR"] | board.pieces["BN"] | board.pieces["BB"] |
                board.pieces["BQ"] | board.pieces["BK"] | board.pieces["BP"]),
            "pieces": board.pieces, 
            "rank_masks": [0xFF, 0xFF00, 0xFF0000, 0xFF000000, 0xFF00000000, 0xFF0000000000, 0xFF000000000000, 0xFF00000000000000],
            "file_masks": [0x101010101010101, 0x202020202020202, 0x404040404040404, 0x808080808080808,
                0x1010101010101010, 0x2020202020202020, 0x4040404040404040, 0x8080808080808080],
            "diagonal_masks": [0x1, 0x102, 0x10204, 0x1020408, 0x102040810, 0x10204081020,
                0x1020408102040, 0x102040810204080, 0x204081020408000, 0x408102040800000,
                0x810204080000000, 0x1020408000000000, 0x2040800000000000, 0x4080000000000000,
                0x8000000000000000],  # Top left to bottom right
            "anti_diagonal_masks": [0x80, 0x8040, 0x804020, 0x80402010, 0x8040201008,
                0x804020100804, 0x80402010080402, 0x8040201008040201, 0x4020100804020100,
                0x2010080402010000, 0x1008040201000000, 0x804020100000000, 0x402010000000000,
                0x201000000000000, 0x100000000000000]  # Top right to bottom left
        }

    def white_pawn_moves(self, pawn, history=None):
        moves_list = ""
        all = self.utilities
        # Common movement, x1x2y1y2
        pawn_moves = (pawn >> 7) & all["black_pieces"] & ~all["rank_8"] & ~all["file_a"]  # Capture right
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i//8 + 1) + str(i%8 - 1) + str(i//8) + str(i%8)
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 9) & all["black_pieces"] & ~all["rank_8"] & ~all["file_h"]  # Capture left
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i//8 + 1) + str(i%8 + 1) + str(i//8) + str(i%8)
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 8) & all["empty"] & ~all["rank_8"]  # Simple move
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i//8 + 1) + str(i%8) + str(i//8) + str(i%8)
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 16) & all["empty"] & ~all["rank_8"] & all["rank_4"]  # Double move
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i//8 + 2) + str(i%8) + str(i//8) + str(i%8)
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        # Promotion y1y2
        pawn_moves = (pawn >> 7) & all["black_pieces"] & all["rank_8"] & ~all["file_a"]  # Capture right and promotion
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i%8 - 1) + str(i%8) + "QP" +vstr(i%8 - 1) + str(i%8) 
            + "RP" + str(i%8 - 1) + str(i%8) + "NP" + str(i%8 - 1) + str(i%8) + "BP"
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 9) & all["black_pieces"] & all["rank_8"] & ~all["file_h"]  # Capture left and promotion
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i%8 + 1) + str(i%8) + "QP" + str(i%8 + 1) + str(i%8) 
            + "RP" + str(i%8 + 1) + str(i%8) + "NP" + str(i%8 + 1) + str(i%8) + "BP"
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        pawn_moves = (pawn >> 8) & all["empty"] & all["rank_8"]  # Simple move and promotion
        possibility = pawn_moves & ~(pawn_moves - 1)
        while(possibility != 0):
            i = trailing_zeros(bin(pawn_moves))
            moves_list += str(i%8) + str(i%8) + "QP" + str(i%8) + str(i%8) 
            + "RP" + str(i%8) + str(i%8) + "NP" + str(i%8) + str(i%8) + "BP"
            pawn_moves &= ~possibility
            possibility = pawn_moves & ~(pawn_moves - 1)
        # En Passant y1y2
        if history:
            if (history[-1][0] == "BP") and (int(history[-1][-1][2]) - int(history[-1][-1][0]) == 2):
                pawn_move = (pawn << 1) & all["pieces"]["BP"] & all["rank_5"] & ~all["file_a"]  # Capture right
                if pawn_move != 0:
                    i = trailing_zeros(bin(pawn_move))
                    moves_list += str(i%8 - 1) + str(i%8) + "E"
                pawn_move = (pawn >> 1) & all["pieces"]["BP"] & all["rank_5"] & ~all["file_h"]  # Capture left
                if pawn_move != 0:
                    i = trailing_zeros(bin(pawn_move))
                    moves_list += str(i%8 + 1) + str(i%8) + "E"
        return moves_list

    def white_bishop_moves(self, bishop):
        moves_list = ""
        all = self.utilities
        i = bishop & ~(bishop - 1)
        while i != 0:
            bishop_spot = trailing_zeros(bin(i))
            bishop_moves = self.diag_moves(bishop_spot) & all["not_white_pieces"]
            j = bishop_moves & ~(bishop_moves - 1)
            while j != 0:
                index = trailing_zeros(bin(j))
                moves_list += str(bishop_spot // 8) + str(bishop_spot % 8) + str(index // 8) + str(index % 8)
                bishop_moves &= ~j
                j = bishop_moves & ~(bishop_moves - 1)
            bishop &= ~i
            i = bishop & ~(bishop - 1)
        return moves_list

    def white_rook_moves(self, rook):
        moves_list = ""
        all = self.utilities
        i = rook & ~(rook - 1)
        while i != 0:
            rook_spot = trailing_zeros(bin(i))
            rook_moves = self.hv_moves(rook_spot) & all["not_white_pieces"]
            j = rook_moves & ~(rook_moves - 1)
            while j != 0:
                index = trailing_zeros(bin(j))
                moves_list += str(rook_spot // 8) + str(rook_spot % 8) + str(index // 8) + str(index % 8)
                rook_moves &= ~j
                j = rook_moves & ~(rook_moves - 1)
            rook &= ~i
            i = rook & ~(rook - 1)
        return moves_list

    def white_queen_moves(self, queen):
        moves_list = ""
        all = self.utilities
        i = queen & ~(queen - 1)
        while i != 0:
            queen_spot = trailing_zeros(bin(i))
            queen_moves = (self.hv_moves(queen_spot) | self.diag_moves(queen_spot)) & all["not_white_pieces"]
            j = queen_moves & ~(queen_moves - 1)
            while j != 0:
                index = trailing_zeros(bin(j))
                moves_list += str(queen_spot // 8) + str(queen_spot % 8) + str(index // 8) + str(index % 8)
                queen_moves &= ~j
                j = queen_moves & ~(queen_moves - 1)
            queen &= ~i
            i = queen & ~(queen - 1)
        return moves_list

    def hv_moves(self, spot):
        all = self.utilities
        binary_s = 1 << spot
        horizontal_moves = (all["occupied"] - 2*binary_s) ^ (reverse(reverse(all["occupied"]) - 2 * reverse(binary_s)))
        vertical_moves = ((all["occupied"] & all["file_masks"][spot % 8]) - (2*binary_s)) ^ \
            (reverse(reverse(all["occupied"] & all["file_masks"][spot % 8]) - 2 * reverse(binary_s)))
        return (horizontal_moves & all["rank_masks"][spot//8]) | (vertical_moves & all["file_masks"][spot%8])

    def diag_moves(self, spot):
        all = self.utilities
        binary_s = 1 << spot
        diagonal_moves = ((all["occupied"] & all["diagonal_masks"][spot // 8 + spot % 8]) - (2*binary_s)) ^ \
            (reverse(reverse(all["occupied"] & all["diagonal_masks"][spot // 8 + spot % 8]) - 2 * reverse(binary_s)))
        anti_diagonal_moves = ((all["occupied"] & all["anti_diagonal_masks"][(spot // 8 + 7) - spot % 8]) - (2*binary_s)) ^ \
            (reverse(reverse(all["occupied"] & all["diagonal_masks"][(spot // 8 + 7) - spot % 8]) - 2 * reverse(binary_s)))
        return (diagonal_moves & all["diagonal_masks"][spot//8 + spot%8]) | (anti_diagonal_moves & all["anti_diagonal_masks"][(spot//8 + 7) - spot%8])
