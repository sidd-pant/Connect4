'''
Siddhartha Pant
Connect4 : Driver File
'''

from connect4game import Connect4Game
from connect4gamesetup import Connect4GameSetup


if __name__ == "__main__":

    setup = Connect4GameSetup()
    
    screen = setup.initialize_screen()

    row_dimension, col_dimension = setup.board_setup()
    board = setup.board_list()

    player_mode_choice = setup.game_mode()

    game = Connect4Game(screen,row_dimension,col_dimension,board,player_mode_choice)
    
    game.game_play()



