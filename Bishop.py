
from ChessPiece import ChessPiece

class Bishop(ChessPiece):

    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self.test = 0

    def display(self):
        return 'b'