
class ChessPiece:

    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player
    
    def display(self):
        return 'x'

    def canMoveTo(self, ending):
        return False