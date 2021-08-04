import turtle
from gamestate import GameState


class Sketch:
    '''
    Class -- Sketch
        Represents a Sketch object which can be used to draw.
    Attributes:
        NUM_SQUARES -- the number of squares on each row
        SQUARE -- the size of each square
        SQUARE_COLORS -- tuple representing the colors of each square
            on the game board
        PLAYER_COLORS -- tuple representing the colors of the checkers
        BOARD_SIZE -- int, representing the size of the game board
        BOTTOM_CORNER -- coordinate of the bottom corner of the board
        pen -- an instance of turtle
    Methods:
        start_UI -- initializes the UI
        draw_square -- helper method, draws a square
        draw_circle -- helper method, draws a circle
        draw_square_outline -- helper method, highlights a squares outline
        draw_checkerboard -- draws game board
        draw_checkerpieces -- draws all checkerpieces in starting position
        get_coordinate -- helper method, returns a corresponding coordinate
            for a row or column
        highlight_squares -- highlights select squares on the game board
        unhighlight_squares -- removes highlighting from select squares on
            the game board
        update_board_for_move -- redraws the board after a CheckerPiece
            object has been moved
        update_board_for_capture -- redraws the board after a CheckerPiece
            object had been moved and captured
        draw_player_piece -- helper method, draws a given CheckerPiece
            object on the board
        draw_game_over -- clears the board and prints winner or
            loser to the screen
        setup_click_handling -- enables clicks to be processed on the UI
    '''
    def __init__(self):
        self.NUM_SQUARES = 8  # The number of squares on each row.
        self.SQUARE = 50  # The size of each square in the checkerboard.
        self.SQUARE_COLORS = ("light gray", "white")
        self.PLAYER_COLORS = ("black", "red")
        self.BOARD_SIZE = self.NUM_SQUARES * self.SQUARE
        self.BOTTOM_CORNER = -self.BOARD_SIZE/2
        self.pen = turtle.Turtle()  # This variable does the drawing.
        self.start_UI()
        self.pen.penup()  # This allows the pen to be moved.
        self.pen.hideturtle()  # This gets rid of the triangle cursor.

    def start_UI(self):
        '''
        Method -- start_UI
            This function sets the size and background color of the UI
                and brings up the graphics window.
        Parameters:
            self -- the current Sketch object
        Returns:
            Nothing. This is only used to set up the UI and make the
                graphics window appear.
        '''
        #  The extra + SQUARE is the margin
        window_size = self.BOARD_SIZE + self.SQUARE
        turtle.setup(window_size, window_size)
        turtle.screensize(self.BOARD_SIZE, self.BOARD_SIZE)
        turtle.bgcolor("white")  # The window's background color
        turtle.tracer(0, 0)  # makes the drawing appear immediately

    def draw_square(self, size):
        '''
        Method -- draw_square
            Draw a square of a given size.
        Parameters:
            self -- the current Sketch object
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
        '''
        SIDES = 4
        RIGHT_ANGLE = 90
        self.pen.begin_fill()
        self.pen.pendown()
        for i in range(SIDES):
            self.pen.forward(size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.end_fill()
        self.pen.penup()

    def draw_circle(self, color, r):
        '''
        Method -- draw_circle
            Draw a circle with a given radius.
        Parameters:
            self -- the current Sketch object
            color -- the color to used to fill the circle
            r -- an int, representing the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics window.
        '''
        self.pen.begin_fill()
        self.pen.color(color, color)
        self.pen.pendown()
        self.pen.circle(radius=r)
        self.pen.penup()
        self.pen.end_fill()

    def draw_square_outline(self, size):
        '''
        Method -- draw_square_outline
            Draws a square without any fill.
        Parameters:
            self -- the current Sketch object
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
        '''
        RIGHT_ANGLE = 90
        SIDES = 4
        self.pen.pendown()
        for i in range(SIDES):
            self.pen.forward(size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.penup()

    def draw_checkerboard(self):
        '''
        Method -- draw_board
            This method draws the checkerboard in the graphics window.
        Parameters:
            self -- the current Sketch object
        Returns:
            Nothing. Draws a white and gray checkerboard in the
                graphics window.
        '''
        self.pen.color("black", self.SQUARE_COLORS[1])
        self.pen.setposition(self.BOTTOM_CORNER, self.BOTTOM_CORNER)
        self.draw_square(self.BOARD_SIZE)
        for col in range(self.NUM_SQUARES):
            for row in range(self.NUM_SQUARES):
                if col % 2 != row % 2:
                    self.pen.color("black", self.SQUARE_COLORS[0])
                    self.pen.setposition(self.BOTTOM_CORNER +
                                         self.SQUARE * col,
                                         self.BOTTOM_CORNER +
                                         self.SQUARE * row)
                    self.draw_square(self.SQUARE)

    def draw_checkerpieces(self):
        '''
        Method -- draw_checkerpieces
            This function draws the checker pieces onto the checkerboard.
        Parameters:
            self -- the current Sketch object
        Returns:
            Nothing. Draws black and red checker pieces in the graphics
                window.
        '''
        RADIUS = self.SQUARE/2
        for col in range(self.NUM_SQUARES):
            for row in range(self.NUM_SQUARES):
                if col % 2 != row % 2:
                    self.pen.setposition(self.BOTTOM_CORNER +
                                         self.SQUARE * col + RADIUS,
                                         self.BOTTOM_CORNER +
                                         self.SQUARE * row)
                    if row <= 2:
                        self.draw_circle(self.PLAYER_COLORS[0], RADIUS)
                    if row >= 5:
                        self.draw_circle(self.PLAYER_COLORS[1], RADIUS)

    def get_coordinate(self, row_col):
        '''
        Method -- get_coordinate
            This method returns the corresponding x, y coordinate
                for a column or row.
        Parameters:
            self -- the current Sketch object
            row_col -- a row or column for which the x or y coordinate
                should be returned
        Returns:
            An x or y coordinate that corresponds to the given row or column.
        '''
        NORMALIZATION_FACTOR = -200
        return (row_col*self.SQUARE) + NORMALIZATION_FACTOR

    def highlight_squares(self, outline_color, squares):
        '''
        Method -- highlight_squares
            This highlights a given set of squares on the game board
                according to a specified color.
        Parameters:
            self -- the current Sketch object
            outline_color -- the color to use to highlight the squares
            squares -- a list, containing board square objects to
                be highlighted
        Returns:
            Nothing. Outputs highlighted squares to the graphics window.
        '''
        self.pen.color(outline_color)
        for square in squares:
            x = self.get_coordinate(square.column)
            y = self.get_coordinate(square.row)
            self.pen.setposition(x, y)
            self.draw_square_outline(self.SQUARE)

    def unhighlight_squares(self, squares):
        '''
        Method -- unhighlight_squares
            Unhighlights the selected squares on the game board.
        Parameters:
            self -- the current Sketch object
            squares -- a list, containing board square objects to
                be unhighlighted
        Returns:
            Nothing. Outputs the game board with the selected
                squares unhighlighted.
        '''
        if squares is not None:
            self.pen.color("black")
            for square in squares:
                x = self.get_coordinate(square.column)
                y = self.get_coordinate(square.row)
                self.pen.setposition(x, y)
                self.draw_square_outline(self.SQUARE)

    def update_board_for_move(
            self, row, col, prior_piece, gamestate: GameState):
        '''
        Method -- update_board_for_move
            This method updates the game board to reflect a players
                move to an empty board square.
        Parameters:
            self -- the current Sketch object
            row -- this is the row in which to move the player's checker piece
            column -- this is the column in which to move the player's
                checker piece
            prior_piece -- this is the Checkerpiece object that is to be
                moved on the game board
            gamestate -- this is a GameState object representing the current
                state of the game
        Returns:
            Nothing. The game board in the UI is updated to reflect the
                piece's move.
        '''
        self.pen.color("black", "light gray")
        self.pen.setposition(
            self.get_coordinate(col), self.get_coordinate(row))
        self.draw_square(self.SQUARE)
        prior_piece_position = prior_piece.get_location_in_squares(
            gamestate.squares)
        self.pen.setposition(self.get_coordinate(prior_piece_position.column),
                             self.get_coordinate(prior_piece_position.row))
        self.pen.color("black", "light gray")
        self.draw_square(self.SQUARE)
        gamestate.update_squares(row, col, prior_piece)
        prior_piece.end_turn(gamestate.squares)
        self.draw_player_piece(row, col, prior_piece)

    def update_board_for_capture(
            self, row, col, prior_spot, jumped_square, gamestate):
        '''
        Method -- update_board_for_capture
            This method updates the game board to reflect a players capturing
                move and removes the captured piece from the game board.
        Parameters:
            self -- the current Sketch object
            row -- this is the row in which to move the player's checker piece
            column -- this is the column in which to move the player's checker
                piece
            prior_piece -- this is the Checkerpiece object that is to be
                moved on the game board
            jumped_square -- the board square containing the captured piece
            gamestate -- this is a GameState object representing the current
                state of the game
        Returns:
            Nothing. The game board in the UI is updated to reflect the
                checker piece's capturing move.
        '''
        self.update_board_for_move(row, col, prior_spot, gamestate)
        self.pen.color("black", "light gray")
        self.pen.setposition(self.get_coordinate(jumped_square.column),
                             self.get_coordinate(jumped_square.row))
        self.draw_square(self.SQUARE)

    def draw_player_piece(self, row, col, piece):
        '''
        Method -- draw_player_piece
            Draws a player piece on the board.
        Parameters:
            self -- the current Sketch object
            row -- the row in which to draw the player piece
            col -- the column in which to draw the player piece
            piece -- the CheckerPiece object that is to be drawn
        Returns:
            Nothing. The board is updated to reflect the specified checkerpiece
                in the given column and row.
        '''
        HALF_SQUARE_SIZE = 25
        FONT_SIZE = 18
        self.pen.setposition(self.get_coordinate(col)+HALF_SQUARE_SIZE,
                             self.get_coordinate(row))
        self.draw_circle(piece.color, self.SQUARE/2)
        if piece.is_king:
            self.pen.goto(self.get_coordinate(col)+HALF_SQUARE_SIZE,
                          self.get_coordinate(row)
                          + HALF_SQUARE_SIZE - FONT_SIZE // 2)
            self.pen.color("gold")
            self.pen.write("K", align="center", font="Arial")

    def draw_game_over(self, msg, color):
        '''
        Method -- draw_game_over
            Updates the board to print a message notifying the user of
                the winner when the game is over.
        Parameters:
            self -- the current Sketch object
            msg -- the message to be printed to the user in addition
                to "Game Over"
            color -- the color of the text that will be printed to the user
        Returns:
            Nothing. Updates the graphics window to be an empty
                checkerboard with the winner of the game printed.
        '''

        self.draw_checkerboard()
        self.pen.setposition(0, -20)
        self.pen.color(color)
        self.pen.write("Game Over!\n  " + msg, align="center",
                       font=("Aharoni", 30, "italic"))

    def setup_click_handling(
            self, click_handling_function):
        '''
        Method -- setup_click_handling
            This uses turtle to call the click handler and
                begin processing user clicks.
        Parameters:
            self -- the current Sketch object
            click_handling_function -- the name of the click handler to use
        Returns:
            Nothing. This calls the click handler which allows user
                clicks to be processed.
        '''
        screen = turtle.Screen()
        # This will call call the click_handler function when a click occurs
        screen.onclick(click_handling_function)
        turtle.done()  # Stops the window from closing.
