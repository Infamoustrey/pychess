
from ChessPiece import ChessPiece
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from King import King
from Queen import Queen

class ChessBoard:

    def __init__(self):

        self.board = []

        # Initialize empty board
        for row in range(8):
            self.board.append([])
            for col in range(8):
                self.board[row].append(ChessPiece(row, col, 0))
        
        # Add Pawns
        for col in range(8):
            self.board[1][col] = Pawn(1,col,1) 
            self.board[6][col] = Pawn(6,col,2) 

        # Add Rooks
        self.board[0][0] = Rook(0,0,1)
        self.board[0][7] = Rook(0,7,1)
        self.board[7][0] = Rook(7,0,2)
        self.board[7][7] = Rook(7,7,2)

        # Add Knights
        self.board[0][1] = Knight(0,1,1)
        self.board[0][6] = Knight(0,6,1)
        self.board[7][1] = Knight(0,1,2)
        self.board[7][6] = Knight(0,6,2)

        # Add Bishops
        self.board[0][2] = Bishop(0,2,1)
        self.board[0][5] = Bishop(0,5,1)
        self.board[7][2] = Bishop(0,2,2)
        self.board[7][5] = Bishop(0,5,2)

        # Add King & Queens
        self.board[0][3] = King(0,2,1)
        self.board[0][4] = Queen(0,5,1)
        self.board[7][3] = King(0,2,2)
        self.board[7][4] = Queen(0,5,2)
        

    def display(self):
        print('  A B C D E F G H')
        
        count = 1
        for row in self.board:
            line = ""
            for piece in row:
                line += piece.display() + ' '
            print( str(count) + ' ' + line)
            count += 1

    def move_piece(self, starting, ending, player):

        if not self.doesPieceExistAtLocation(starting):
            return 'No Piece to move at that location, try another!'
        elif not self.doesPieceAtLocationBelongToPlayer(starting, player) :
            return 'That piece is not yours to move!'
        else:
            return ''
    
    # Checks to see if a piece exists on the board at a given location
    def doesPieceExistAtLocation(self, starting):
        return self.board[ starting[0] ][ starting[1] ].__class__.__name__ != 'ChessPiece'

    # Checks to see if a piece at a given location belongs to the player
    def doesPieceAtLocationBelongToPlayer(self, starting, player): 
        return self.board[ starting[0] ][ starting[1] ].player == player