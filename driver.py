'''
Siddhartha Pant
CS 5001 Spring 2020
Final Project
April 8, 2020
'''

from connect4game import Connect4Game
from connect4gamesetup import Connect4GameSetup


def main():

    # declare an object from the Connect4GameSetup Class
    setup = Connect4GameSetup()

    # initialize the game sreen
    screen = setup.initialize_screen()

    # set up the game board list
    row_dimension, col_dimension = setup.board_setup()
    board = setup.board_list()

    # retrieve the mode of play chosen by the player
    player_mode_choice = setup.game_mode()

    # declare an object from the Connect4Game Class
    game = Connect4Game(screen,row_dimension,col_dimension,board,player_mode_choice)

    # execute the game_play method to run the game
    game.game_play()


main()