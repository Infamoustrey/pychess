from Game import Game

game = Game()
 
# Start the Main Game Loop, keep running as long as the game is not over
while game.isGameRunning:
    game.run()

# Close the program
exit(0)