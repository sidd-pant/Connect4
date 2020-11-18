# Connect4
Connect4 Game in Python (GUI through Turtle)


This program implements the Connect4 Game in python using the Turtle Library. Players can play Human vs Human or Human vs Computer.

Connect4GameSetup Class:
This class implements methods that set up the majority of the visual aspects of the game for the player (initialising the screen, 
selecting mode of game: human vs computer or human vs human, setting up the game board and selecting row and column dimensions) and 
set ups the initial game board (list) for the program to manipulate for game functions.

Class4GameFunctions Class:
This class implements all the back end functions of the game, including positioning the player's move correctly in the board list, 
determining if the player's move is valid, finding the next open row, checking for winning and draw results, and determining computer's 
move selection in the context of a Human vs Computer play. This class also keeps track of the number of games won by each players and 
saves progress into a file to read from. 

Connect4Game Class:
This class implements a method for the game play aspect of the game, including user input on move and calling relevant methods 
from Connect4GameFunctions and Connect4Display classes to execute the game and display it to the players.

Connect4Display Class:
This class implements the display functions of the program, including the display of the game grid, outcome of the game, current 
win count for each players and the option for the user to close the turtle screen upon clicking.

Driver: 
The main method declares an object from the Connect4GameSetup class and first calls the method to initialise the screen. Then the 
board is setup based on user input for row and column dimension. After that the method for game mode is called to seek user input 
regarding where the user wants to play Human vs Human or Human vs Computer. The screen, row dimension, column dimension and player 
mode choice are then passed into an object of the Connect4Game class to execute the game play method.
