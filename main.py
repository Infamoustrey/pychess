
from ChessBoard import ChessBoard

board = ChessBoard()

# Game Variables
isGameRunning = True
isLookingAtHelp = False
currentPlayer = 1

def switchPlayers(currentPlayer):
    if currentPlayer == 1:
        currentPlayer = 2
    elif currentPlayer == 2:
        currentPlayer = 1
    return 

def parseInput(input, isLookingAtHelp):

    if input == 'c':
        print('Closing Game...')
        exit(0)
    
    if isLookingAtHelp:
        if input == 'q':
            isLookingAtHelp = False
        else: 
            return 
    elif parseMove(input):
        return 

def parseMove(input):
    return 

def displayHelp():
    
    print('')

# Start the Main Game Loop, keep running as long as the game is not over
while isGameRunning:

    # Clear the Terminal
    print(f"\033c")
    
    # Display either the board or the help screen
    if not isLookingAtHelp:
        board.display()
    else:
        displayHelp()

    # Prompt and take that input
    parseInput( input('Player ' + str(currentPlayer) + ' make a move(enter ? for help):'), isLookingAtHelp )

    

 