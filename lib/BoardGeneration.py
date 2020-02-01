class BoardGeneration(object):
    def __init__(self):
        self.chessBoard = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        self.typesOfPieces = {"WR": 0, "WN": 0, "WB": 0, "WQ": 0, "WK": 0,
                "WP": 0, "BR": 0, "BN": 0, "BB": 0, "BQ": 0, "BK": 0, "BP": 0}
        self.pieces = self.set_pieces()

    def set_pieces(self):
        pieces = self.typesOfPieces
        i = 0
        binary = 0b01
        for i in range(64):
            spot = self.chessBoard[i//8][i % 8]
            if spot == "R":
                pieces["WR"] += binary
            elif spot == "N":
                pieces["WN"] += binary
            elif spot == "B":
                pieces["WB"] += binary
            elif spot == "Q":
                pieces["WQ"] += binary
            elif spot == "K":
                pieces["WK"] += binary
            elif spot == "P":
                pieces["WP"] += binary
            elif spot == "r":
                pieces["BR"] += binary
            elif spot == "n":
                pieces["BN"] += binary
            elif spot == "b":
                pieces["BB"] += binary
            elif spot == "q":
                pieces["BQ"] += binary
            elif spot == "k":
                pieces["BK"] += binary
            elif spot == "p":
                pieces["BP"] += binary
            binary = binary << 1
        return pieces

    def drawArray(self):
        pieces = self.pieces
        board = []
        i = 0
        for i in range(8):
            board.append([" "] * 8)
        i = 0
        for i in range(64):
            if (((pieces["WR"] >> i) & 1) == 1):
                board[i//8][i % 8] = "R"
            elif (((pieces["WN"] >> i) & 1) == 1):
                board[i//8][i % 8] = "N"
            elif (((pieces["WB"] >> i) & 1) == 1):
                board[i//8][i % 8] = "B"
            elif (((pieces["WQ"] >> i) & 1) == 1):
                board[i//8][i % 8] = "Q"
            elif (((pieces["WK"] >> i) & 1) == 1):
                board[i//8][i % 8] = "K"
            elif (((pieces["WP"] >> i) & 1) == 1):
                board[i//8][i % 8] = "P"
            elif (((pieces["BR"] >> i) & 1) == 1):
                board[i//8][i % 8] = "r"
            elif (((pieces["BN"] >> i) & 1) == 1):
                board[i//8][i % 8] = "n"
            elif (((pieces["BB"] >> i) & 1) == 1):
                board[i//8][i % 8] = "b"
            elif (((pieces["BQ"] >> i) & 1) == 1):
                board[i//8][i % 8] = "q"
            elif (((pieces["BK"] >> i) & 1) == 1):
                board[i//8][i % 8] = "k"
            elif (((pieces["BP"] >> i) & 1) == 1):
                board[i//8][i % 8] = "p"
        return board
