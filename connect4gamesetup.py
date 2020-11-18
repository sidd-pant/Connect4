'''
Siddhartha Pant
Connect4
'''

import turtle

class Connect4GameSetup():
    '''
        Class: Connect4GameSetup
        Description: This class encapsulates methods that set up the majority of
        the visual aspects of the game for the player (initializing the screen,
        selecting mode of game: human vs computer or human vs human, setting up the
        game board and selecting row and column dimensions) and set ups the initial
        game board (list) for the program to manipulate for game functions.
        Attributes: screen
                    row_dimension
                    col_dimension
        Methods: initialize_screen
                game_mode
                board_setup
                board_list
    '''

    def __init__(self, screen = "", row_dimension = 6, col_dimension = 7):
        '''
        Constructor: creates new instance of Connect4GameSetup
        Parameters: self (current object), screen, row_dimension, col_dimension
        '''

        self.screen = screen
        self.row_dimension = row_dimension
        self.col_dimension = col_dimension

    def initialize_screen(self):
        '''
        Method: initialize_screen
        Parameter: self
        Does: initializes the turtle screen, sets background color and updates
        the class attribute pertaining to the screen
        Returns: screen
        '''

        screen = turtle.Screen()
        screen.screensize(750, 750)
        screen.bgcolor("light grey")

        self.screen = screen

        return screen

    def board_setup(self):
        '''
        Method: board_setup
        Parameter: self
        Does: enters the title, seeks user input for row and column dimension,
        and sets up a game board based on dimensions. In addition, updates the
        class attribute pertaining to the row and column dimensions.
        Returns: row_dim (row dimension), col_dim (column dimension)
        '''

        DISC_SPACING = 50
        
        title = turtle.Turtle()

        title.color("black")
        style = ('PT Sans', 50, 'bold')
        title.hideturtle()
        title.penup()
        title.goto(-35, 250)
        title.pendown()
        title.write('Connect Four', align='center', font=('PT Sans', 40, 'bold'))
        title.penup()
        title.goto(220, 260)
        title.write('Result:', align='center', font=('PT Sans', 20, 'underline'))

        row_dim = int(self.screen.numinput("Row Dimension",
                "Enter your Row Dimension:", 6, minval=4, maxval=8))
        col_dim = int(self.screen.numinput("Column Dimension",
                "Enter your Col Dimension:", 7, minval=4, maxval=10))
        
        game_board = turtle.Turtle()
        game_board.hideturtle()
        game_board.speed(0)

        game_board.penup()
        game_board.goto(-300, 225)
        game_board.pendown()

        width = row_dim * (DISC_SPACING + 10)
        length = col_dim * (DISC_SPACING + 10)

        game_board.fillcolor("blue")
        game_board.begin_fill()

        game_board.forward(length)
        game_board.right(90)

        game_board.forward(width)
        game_board.right(90)

        game_board.forward(length)
        game_board.right(90)

        game_board.forward(width)
        game_board.right(90)

        game_board.end_fill()

        self.row_dimension = row_dim
        self.col_dimension = col_dim

        return row_dim, col_dim

    def game_mode(self):
        '''
        Method: game_mode
        Parameter: self
        Does: seeks user input for game mode: Human vs Human or Human vs Computer
        Returns: user's choice (H for human vs human, C for human vs computer)
        '''

        human_or_computer = self.screen.textinput("Choose the mode of the game",
                            "Human vs Human(H) or Human vs Computer (C)")
        human_or_computer = human_or_computer.upper()

        while human_or_computer != 'H' and human_or_computer != 'C':
            human_or_computer = self.screen.textinput(
                                "Invalid input. Choose the mode of the game",
                                "Human vs Human(H) or Human vs Computer (C)")
            human_or_computer = human_or_computer.upper()

        return human_or_computer

    def board_list(self):
        '''
        Method: board_list
        Parameter: self
        Does: sets up the initial game board (list) based on user's desired
        row and column dimensions
        Returns: game board (list)
        '''

        EMPTY_DISC = 0
        
        matrix = [[EMPTY_DISC for col in range(self.col_dimension)]
                  for row in range(self.row_dimension)]
        return matrix

