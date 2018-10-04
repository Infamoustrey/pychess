from ChessPiece import ChessPiece

class Pawn(ChessPiece):

    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self.test = 0

    def display(self):
        return 'p'

    def canMoveTo(self, ending):
        mod = 0
        firstMove = False  
        if self.player == 1:
            mod = -1 
            if row == 1:
                firstMove = True
        elif self.player == 2:
            mod = 1
            if row == 6:
                firstMove = True
        
        
        
        