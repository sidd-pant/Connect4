'''
Siddhartha Pant
Connect4
'''

import turtle


class Connect4Display:
    '''
    Class: Connect4Display
    Description: This class encapsulates the display functions of the program,
                including the display of the game grid, current win count for each
                players, outcome of the current game and the option for the user to
                close the turtle screen upon clicking.
    Attributes: screen, board (list)
                row_dim (row dimension)
                col_dim (column dimension)
    Methods: game_grid
            display_result
            display_win_count
            close_screen
    '''

    def __init__(self, screen, row_dim, col_dim, board):
        '''
        Constructor: creates new instance of Connect4Display
        Parameters: self (current object), screen, row_dim, col_dim, board
        '''

        self.screen = screen
        self.row_dim = row_dim
        self.col_dim = col_dim
        self.board = board

    def game_grid(self):
        '''
        Method: game_grid
        Parameter: self
        Does: uses turtle to convert a list into game grid with circles and fill
            appropriate disc color. Adds numerical labels to grid columns to
            support user input
        Returns: nothing
        '''

        DISC_SIZE = 20
        DISC_SPACING = 50
        YELLOW_DISC = 1
        RED_DISC = 2

        
        flip_board = [element for element in reversed(self.board)]

     
        disc = turtle.Turtle()
        disc.hideturtle()

      
        disc.speed(0)

        
        disc.setheading(0)
        disc.penup()
        disc.goto(-250, 170)

       
        for row in range(0, self.row_dim):
            for col in range(0, self.col_dim):
                if flip_board[row][col] == 0:
                    disc.fillcolor("white")
                elif flip_board[row][col] == YELLOW_DISC:
                    disc.fillcolor("yellow")
                elif flip_board[row][col] == RED_DISC:
                    disc.fillcolor("red")

                disc.begin_fill()
                disc.circle(DISC_SIZE)
                disc.end_fill()

                disc.penup()
                
                disc.forward(DISC_SPACING)

            disc.setheading(270)
            disc.forward(DISC_SPACING)
            disc.setheading(180)
            disc.forward(DISC_SPACING * self.col_dim)
            disc.setheading(0)
            
        column_header = turtle.Turtle()
        column_header.hideturtle()
        column_header.penup()
        column_header.goto(-250, 225)

        for col in range(0, self.col_dim):
            column_header.color("black")
            style = ('PT Sans', 50, 'bold')
            column_header.write(col + 1, align='center', font=('PT Sans', 15, 'bold'))
            column_header.penup()
            column_header.forward(50)

    def display_result(self, result):
        '''
        Method: display_result
        Parameter: self, result (a string indicating which disc won)
        Does: uses turtle to display the outcome of the game - winner or draw
        Returns: nothing
        '''
        outcome = turtle.Turtle()
        outcome.hideturtle()
        outcome.penup()
        outcome.goto(220, 240)

        if result == "yellow":
            outcome.color("black")
            outcome.write("YELLOW WINS", True, align="center",
                          font=("PT Sans", 20, "normal"))
            outcome.pendown()
            outcome.getscreen().update()

        if result == "red":
            outcome.color("black")
            outcome.write("RED WINS", True, align="center",
                          font=("PT Sans", 20, "normal"))
            outcome.pendown()
            outcome.getscreen().update()

        if result == "draw":
            outcome.penup()
            outcome.color("white")
            outcome.write("IT'S A DRAW", True, align="center",
                          font=("Arial", 20, "normal"))
            outcome.pendown()
            outcome.getscreen().update()
        

    def display_win_count(self,current_score_yellow, current_score_red):
        '''
        Method: display_win_count
        Parameter: self, current_score_yellow(int), current_score_red(int)
        Does: displays total win scores for yellow and red in the turtle windoow
        Returns: nothing
        '''

        count = turtle.Turtle()
        count.hideturtle()
        count.penup()
        count.color("black")
        count.goto(-35,-230)

        count.write("Win Count Yellow:", True, align="center", font=("PT Sans", 20, "bold"))
        count.goto(-25,-250)
        count.write(current_score_yellow, True, align="center", font=("PT Sans", 20, "bold"))
        count.goto(-35,-280)

        count.write("Win Count Red:", True, align="center", font=("PT Sans", 20, "bold"))
        count.goto(-25,-300)
        count.write(current_score_red, True, align="center", font=("PT Sans", 20, "bold"))
        count.pendown()
        count.getscreen().update()

    def close_screen(self):
        '''
        Method: close_screen
        Parameter: self
        Does: allows user to exit the turtle screen on click
        Returns: nothing
        '''

        screen = turtle.Screen()
        screen.screensize(750, 750)
        turtle.Screen().exitonclick()
