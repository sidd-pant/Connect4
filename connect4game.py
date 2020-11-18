'''
Siddhartha Pant
CS 5001 Spring 2020
Final Project
April 8, 2020
'''

from connect4display import Connect4Display
from connect4gamefunctions import Connect4GameFunctions

EMPTY_DISC = 0
YELLOW_DISC = 1
RED_DISC = 2

class Connect4Game():
    '''
        Class: Connect4Game
        Description: This class encapsulates a method for the game play aspect
                    of the game, including user input on move and calling relevant
                    methods from Connect4GameFunctions and Connect4Display classes
                    to execute the game and display it to the players.
        Attributes: screen
                    row_dimension
                    col_dimension
                    board
                    player_mode_choice
        Method: game_play
    '''

    def __init__(self, screen, row_dimension, col_dimension, board, player_mode_choice):
        '''
        Constructor: creates new instance of Connect4Game
        Parameters: self (current object), row_dimension, col_dimension, board,
                    player_mode_choice
        '''
        self.screen = screen
        self.row_dimension = row_dimension
        self.col_dimension = col_dimension
        self.board = board
        self.player_mode_choice = player_mode_choice


    def game_play(self):
        '''
        Method: game_play
        Parameters: self
        Does: seeks user input on moves, and calls relevant methods from
            Connect4GameFunctions and Connect4Display classes to execute
            the game and display game proceedings to the players.
        Returns: nothing
        
        '''

        YELLOW_DISC = 1
        RED_DISC = 2


        # declaring an object from the Connect4Display class 
        graphics = Connect4Display(self.screen, self.row_dimension,
                                   self.col_dimension, self.board)
        # calling the game_grid method
        graphics.game_grid()

        # declaring an object from the game_functions class
        game_functions = Connect4GameFunctions(self.row_dimension,
                                               self.col_dimension,self.board)


        # using a boolean to track when the game ends
        end_of_game = False

        # initialize a variable switch to keep track of alternating turns
        switch = 0

        # get total win count by reading into the red and yellow files
        file1 = "yellow" + ".txt"
        current_score1 = game_functions.count_wins(file1)
        file2 = "red" + ".txt"
        current_score2 = game_functions.count_wins(file2)

        # displays win counts in turtle window
        graphics.display_win_count(current_score1, current_score2)

        while not end_of_game:
            # yellow's turn
            if switch == 0:
                user_input_col = int(self.screen.numinput("Yellow",
                            "In which column number, do you want to put your disc?",
                            minval=1, maxval= self.col_dimension))
                # adjusting user input for list index
                user_input_col -= 1
                # at each input for yellow, change the switch value to 1
                switch += 1

                # until user's move is invalid, prompt the user for input 
                while not game_functions.valid_move(user_input_col):
                    user_input_col = int(self.screen.numinput("Yellow",
                            "Board space occupied, enter valid move", minval=1,
                            maxval=self.col_dimension))
                    user_input_col -= 1

                # find corresponding row, drop the disc and update user interface
                if game_functions.valid_move(user_input_col):
                    corresponding_row = game_functions.find_next_open_row(user_input_col)
                    game_functions.drop_disc(corresponding_row, user_input_col,
                                             YELLOW_DISC)
                    graphics.game_grid()

                    # if yellow wins, display the result and end the game
                    if game_functions.winning_result(1) == True:
                        result = "yellow"
                        graphics.display_result(result)
                        # update win count upon each successful win
                        game_functions.update_file(file1)
                        end_of_game = True


            # red's turn
            else:
                # check if user selected Human vs Computer
                # if user selected human vs computer, call computer play method
                if self.player_mode_choice == 'C':
                    user_input_col = game_functions.computer_play()

                # if user selected human vs human, seek player input
                else:
                    user_input_col = int(self.screen.numinput("Red",
                            "In which column number, do you want to put your disc?",
                            minval=1, maxval=self.col_dimension))
                    # adjusting user input for list index
                    user_input_col -= 1

                # at each input for red, change the value of switch to zero
                switch -= 1

                # until user's move is invalid, prompt the user for input
                while not game_functions.valid_move(user_input_col):
                    user_input_col = int(self.screen.numinput("Player Two",
                                "Board space occupied, enter valid move", minval=1,
                                maxval=self.col_dimension))
                    user_input_col -= 1

                # find corresponding row, drop the disc and update user interface
                if game_functions.valid_move(user_input_col):
                    corresponding_row = game_functions.find_next_open_row(user_input_col)
                    game_functions.drop_disc(corresponding_row, user_input_col,
                                             RED_DISC)
                    graphics.game_grid()

                    # if red wins, display the result and end the game
                    if game_functions.winning_result(2) == True:
                        result = "red"
                        graphics.display_result(result)
                        # update win count upon each successful win
                        game_functions.update_file(file2)
                        end_of_game = True

                # if the games is drawn, display the result and end the game
                if game_functions.draw_result() == True:
                    result = "draw"
                    graphics.display_result(result)
                    end_of_game = True

        # close the screen on click
        graphics.close_screen()
