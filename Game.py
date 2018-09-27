
from ChessBoard import ChessBoard
import re

class Game:

    def __init__(self):

        # Game variables
        self.board = ChessBoard()
        self.isGameRunning = True
        self.showHelp = False
        self.currentPlayer = 1
        self.turnCount = 0
        self.inputErrorMessage = ''

        # Read help file into memory
        with open('help.txt', 'r') as fp:
            self.helpfile = fp.readlines()
            self.helpfile = [line.rstrip('\n') for line in self.helpfile]

    def switchPlayers(self):
        if self.currentPlayer == 1:
            self.currentPlayer = 2
        elif self.currentPlayer == 2:
            self.currentPlayer = 1
        self.turnCount += 1

    def parseInput(self, input):

        self.inputErrorMessage = ''

        if input == '':
            return

        if input == 'c':
            print('Closing Game...')
            self.isGameRunning = False
            return 

        if input == '?':
            if not self.showHelp:
                self.showHelp = True
                return 
                
        if input == 'q':
            if self.showHelp:
                self.showHelp = False 
                return

        if input == 'pass':
            if not self.showHelp: 
                self.switchPlayers()
                return  
        
        # Check if the move command is valid, (in he-man narrator's voice)BEHOLD REGEX: I HAVE THE POWER!
        # should match move {piece staring position} to {piece ending position}
        if re.match(r"move\s[a-hA-H][1-8]\sto\s[a-hA-H][1-8]", input):
            self.parseMove(input)
       

    def parseMove(self, input):
        # grab positions
        positions = re.findall(r"([a-hA-H][1-8])", input)
        if len(positions) != 2:
            self.inputErrorMessage = 'Not a valid move command'
        
        if ord(positions[0][0]) < 97:
            characterOffset = 65
        else:
            characterOffset = 97

        startingPosition = [0,0]
        startingPosition[0] = ord(positions[0][0]) - characterOffset
        startingPosition[1] = int(positions[0][1]) - 1
        
        endingPosition = [0,0]
        endingPosition[0] = ord(positions[1][0]) - characterOffset
        endingPosition[1] = int(positions[1][1]) - 1

        self.inputErrorMessage = self.board.move_piece(startingPosition, endingPosition, self.currentPlayer)

        print(self.inputErrorMessage)
        exit(0)




    def prompt(self):
        if self.showHelp:
            return input('Press q to close help: ')
        else:
            return input('Player ' + str(self.currentPlayer) + ' make a move(enter ? for help): ')

    def displayHelp(self):  
        for line in self.helpfile:
            print(line)
 
    def run(self):

        # Clear the Terminal
        print(f"\033c")
        
        # Display either the board or the help screen
        if not self.showHelp:
            print('Turn Counter: ' + str(self.turnCount) )
            print(' ')
            self.board.display()
        else:
            self.displayHelp()

        if len(self.inputErrorMessage) > 0: 
            print('Invalid Input: ' + self.inputErrorMessage)

        # Prompt and take that input
        self.parseInput( self.prompt() )


     








    

    

 