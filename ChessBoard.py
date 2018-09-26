
from ChessPiece import ChessPiece

class ChessBoard:

    def __init__(self):

        self.board = []

        for row in range(8):
            self.board.append([])
            for col in range(8):
                self.board[row].append(ChessPiece)

    def display(self):
        for row in self.board:
            line = ""
            for piece in row:
                line += piece.display() + ' '
            print(line)