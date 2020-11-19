'''
Siddhartha Pant
Connect4
'''

import random
import os

class Connect4GameFunctions:
    
    '''
    Class: Connect4GameFunctions
    Description: This class  encapsulates all the back end functions of the game,
                including positioning the player's move correctly in the board list, 
                determining if the player's move is valid, finding the next open row,
                checking for winning and draw results, and determining computer's
                move selection in the context of a Human vs Computer play. Furthermore,
                it tracks the total number of games won by each of the player and saves it
                in the file
    Attributes: board (list)
                row_dim (row dimension),
                col_dim (column dimension)
    Methods: drop_disc
            valid_move
            find_next_open_row
            winning_result
            draw_result
            computer_play
            count_wins
            update_file
    '''

    def __init__(self, row_dim, col_dim, board):
        '''
        Constructor: creates new instance of Connect4GameFunctions
        Parameters: self (current object), row_dim, col_dim, board
        '''

        self.row_dim = row_dim
        self.col_dim = col_dim
        self.board = board

    def drop_disc(self,corresponding_row, user_input_col, disc):
        '''
        Method: drop_disc
        Parameter: self, corresponding_row, user_input_col(player's move),
                  disc(keeps track of which player is playing)
        Does: positions the player's move correctly into the board list
        Returns: nothing
        '''
        
        self.board[corresponding_row][user_input_col] = disc


    def valid_move(self,user_input_col):
        '''
        Method: valid_move
        Parameter: self, user_input_col(player's move)
        Does: checks if the player's move is valid
        Returns: a boolean (True for valid move, False for invalid move)
        '''
        
        return self.board[self.row_dim - 1][user_input_col] == 0

    def find_next_open_row(self, user_input_col):
        '''
        Method: find_next_open_row
        Parameters: self, user_input_col(player's move)
        Does: finds the next open row to place disc based on player's move
        Returns: row (an integer, valid row index of the board list)
        '''

        for row in range(self.row_dim):
            if self.board[row][user_input_col] == 0:
                return row

    def winning_result(self, disc):
        '''
        Method: winning_result
        Parameters: self, disc (keeps track of which player is playing)
        Does: checks the board list for trends for a winning result
            (each player forming a horizontal, vertical or diagonal
        streak with 4 consecutive discs)
        Returns: boolean (True if the outcome is a win, False if it is not)
        '''
        
        # checking for a horizontal streak of 4 consecutive same colored discs
        for column in range(self.col_dim - 3):
            for row in range(self.row_dim):
                if (
                    self.board[row][column] == disc and
                    self.board[row][column + 1] == disc and
                    self.board[row][column + 2] == disc and
                    self.board[row][column + 3] == disc
                ):
                    return True

         # checking for a horizontal streak of 4 consecutive same colored discs
        for column in range(self.col_dim):
            for row in range(self.row_dim - 3):
                if (
                    self.board[row][column] == disc and
                    self.board[row + 1][column] == disc and
                    self.board[row + 2][column] == disc and
                    self.board[row + 3][column] == disc
                ):
                    return True

        # checking for diagonal streak in the 'right' direction
        for column in range(self.col_dim - 3):
            for row in range(self.row_dim - 3):
                if (
                    self.board[row][column] == disc and
                    self.board[row + 1][column + 1] == disc and
                    self.board[row + 2][column + 2] == disc and
                    self.board[row + 3][column + 3] == disc
                ):
                    return True

        # checking for diagonal streak in the 'left' direction 
        for column in range(self.col_dim - 3):
            for row in range(3, self.row_dim):
                if (
                    self.board[row][column] == disc and
                    self.board[row - 1][column + 1] == disc and
                    self.board[row - 2][column + 2] == disc and
                    self.board[row - 3][column + 3] == disc
                ):
                    return True

        # if no winning trends found, return False
        return False

    def draw_result(self):
        '''
        Method: draw_result
        Parameters: self
        Does: checks if the board list has all elements filled with player's moves
        Returns: boolean (True if the outcome is a draw, False if it is not)
        '''

        count = 0

        for column in range(self.col_dim):
            for row in range(self.row_dim):
                if self.board[row][column] != 0:
                    count += 1
                    
        if count == (self.row_dim * self.col_dim):
            return True

        return False

    def computer_play(self):
        '''
        Method: computer_play
        Parameters: self
        Does: returns player's move for the computer in a Human vs Computer game
        Returns: computer's move
        '''
        
        computer_input_col = random.randint(1, self.col_dim)
        computer_input_col -= 1

        while not self.valid_move(computer_input_col):
            computer_input_col = random.randint(1, self.col_dim)
            computer_input_col -= 1
            
            if self.draw_result() == True:
                break

        return computer_input_col

    def count_wins(self,file):
        '''
        Method: count_wins
        Parameters: a file that is locally stored and has player information
        Does: counts all the games that have been won by each player.
        Begins with count 0, and updates an existing file if it exists. Otherwise,
        returns that the player has not won any puzzles. 
        Returns: count of win
        '''

        win_count = 0

        if not os.path.exists(file):
            with open(file, "w") as num_wins:
                num_wins.write(str(win_count))
                
        try:
            with open(file, "r") as num_wins:
                return num_wins.readline()
        except FileNotFoundError:
            print("\nYou have solved 0 puzzles till date")

    def update_file(self,file):
        '''
        Function Name: update_file
        Parameters: a file that is locally stored and has player information
        Does: Updates the file with the total number of games won for each
        player by reading the file and then increasing the count. 
        '''
        try:
            with open(file, "r") as update_file:
                current_count = int(update_file.readline())
                current_count += 1
            with open(file, "w") as outfile:
                outfile.write(str(current_count))
        except IOError:
            print("Couldn't update  - must try again later")








