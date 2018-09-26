
from ChessPiece import ChessPiece

class Queen(ChessPiece):

    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self.test = 0

    def display(self):
        return 'q'