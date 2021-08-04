from checkerpiece import CheckerPiece


class GameState:
    '''
    Class -- GameState
        Represents the state of the game
    Attributes:
        squares -- a list of lists that represent each square on the board game
        current_player -- the player whose turn it is
        red_count -- the number of red checkerpiece objects on the board
        black_count -- the number of black checkerpiece objects on the board
    Methods:
        piece_selected -- Gets the CheckerPiece object at a given
            column and row
        get_valid_pieces -- Gets the CheckerPiece objects that can be moved
        get_valid_squares -- Gets the BoardSquare objects containing
            CheckerPiece Objects which can be moved
        get_black_count -- Gets the number of black CheckerPieces
            remaining in the game
        get_red_count -- Gets the number of red CheckerPieces remaining
            in the game
        end_move -- resets the current_player and indicates whether
            the game should continue after a
            non-capturing move
        end_capture_move -- resets the current_player and indicates
            whether the game should continue after a capturing move
        update_squares -- updates the list of lists after a move has been made
    '''

    def __init__(self):
        '''
        Constructor -- creates a new instance of GameState
        Parameters:
            self -- the current GameState object
        '''
        self.squares = [[None, CheckerPiece("BLACK"), None,
                        CheckerPiece("BLACK"), None, CheckerPiece("BLACK"),
                        None, CheckerPiece("BLACK")],
                        [CheckerPiece("BLACK"), None,
                        CheckerPiece("BLACK"), None, CheckerPiece("BLACK"),
                        None, CheckerPiece("BLACK"), None],
                        [None, CheckerPiece("BLACK"), None,
                        CheckerPiece("BLACK"), None, CheckerPiece("BLACK"),
                        None, CheckerPiece("BLACK")],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [CheckerPiece("RED"), None, CheckerPiece("RED"), None,
                        CheckerPiece("RED"), None, CheckerPiece("RED"), None],
                        [None, CheckerPiece("RED"), None, CheckerPiece("RED"),
                        None, CheckerPiece("RED"), None, CheckerPiece("RED")],
                        [CheckerPiece("RED"), None, CheckerPiece("RED"), None,
                        CheckerPiece("RED"), None, CheckerPiece("RED"), None]]
        self.current_player = "BLACK"
        self.red_count = 12
        self.black_count = 12

    def piece_selected(self, row, column):
        '''
        Method -- piece_selected
            Returns a CheckerPiece object located on the game
                board given a specific location
        Parameters:
            self -- the current GameState object
            row -- the row/index to search
            column -- the column/index to search
        Returns:
            A CheckerPiece object, located at the given row and column.
        '''
        piece_selected = self.squares[row][column]
        return piece_selected

    def get_valid_pieces(self):
        '''
        Method -- get_valid_pieces
            Scans the game board and returns a list of all CheckerPiece objects
                that can legally be moved for the current player.
        Parameters:
            self -- the current GameState object
        Returns:
            A list of CheckerPiece objects belonging to the current
                player which can legally be moved on the game board.
        '''
        NUM_ROW_COL = 8
        valid_pieces = []
        capturing_pieces = []
        for i in range(0, NUM_ROW_COL):
            for j in range(0, NUM_ROW_COL):
                piece = self.squares[i][j]
                if piece is not None and piece.color == self.current_player:
                    if piece.can_capture(self.squares):
                        capturing_pieces.append(piece)
                    else:
                        moves = piece.get_possible_moves(self.squares)
                        if len(moves) != 0:
                            valid_pieces.append(piece)
        if len(capturing_pieces) != 0:
            valid_pieces = capturing_pieces
        return valid_pieces

    def get_valid_squares(self):
        '''
        Method -- get_valid_squares
            Scans the game board and returns a list of all the BoardSquare
                objects from which CheckerPiece Objects can be legally
                moved for the current player.
        Parameters:
            self -- the current GameState object
        Returns:
            A list of BoardSquare objects which can legally be selected
                by the current player.
        '''
        NUM_ROW_COL = 8
        valid_squares = []
        capturing_squares = []
        for i in range(0, NUM_ROW_COL):
            for j in range(0, NUM_ROW_COL):
                piece = self.squares[i][j]
                if piece is not None and piece.color == self.current_player:
                    square = piece.get_location_in_squares(self.squares)
                    if piece.can_capture(self.squares):
                        capturing_squares.append(square)
                    else:
                        moves = piece.get_possible_moves(self.squares)
                        if len(moves) != 0:
                            valid_squares.append(square)
        if len(capturing_squares) != 0:
            valid_squares = capturing_squares
        return valid_squares

    def get_black_count(self):
        '''
        Method -- get_black_count
            Identifies how many black CheckerPiece objects are left
                remaining on the board.
        Parameters:
            self -- the current GameState object
        Returns:
            An int, representing the number of black CheckerPiece objects
                left on the board.
        '''
        return self.black_count

    def get_red_count(self):
        '''
        Method -- get_red_count
            Identifies how many red CheckerPiece objects are left
                remaining on the board.
        Parameters:
            self -- the current GameState object
        Returns:
            An int, representing the number of red CheckerPiece
                objects left on the board.
        '''
        return self.red_count

    def end_move(self):
        '''
        Method -- end_move
            Ends a move by switching the current player and returning True if
                the game is over or False if the game should continue.
        Parameters:
            self -- the current GameState object
        Returns:
            A boolean indicating whether the game has ended.
        '''
        if self.current_player == "BLACK":
            self.current_player = "RED"
        else:
            self.current_player = "BLACK"
        options_left = self.get_valid_pieces()
        if len(options_left) == 0:
            return True
        return False

    def end_capture_move(self, prior_checker_selected, jumped_square):
        '''
        Method -- end_capture_move
            Ends a turn after a capturing move is made by updating
                the gamestate, switching the current_player, and returning
                True if the game is over or False if the game should continue.
        Parameters:
            prior_checker_selected -- A CheckerPiece object representing the
                piece that was just moved to complete a capture.
            jumped_square -- A BoardSquare object representing the square
                containing the piece that was captured.
        Returns:
            A boolean indicating whether the game has ended.
        '''
        no_options_left = False
        prior_checker_selected.end_turn(self.squares)
        if prior_checker_selected.color == "BLACK":
            self.red_count -= 1
        else:
            self.black_count -= 1
        self.squares[jumped_square.row][jumped_square.column] = None
        if not prior_checker_selected.can_capture(self.squares):
            no_options_left = self.end_move()
        if self.red_count == 0 or self.black_count == 0 or no_options_left:
            return True
        return False

    def update_squares(self, row, column, prior_checker_selected):
        '''
        Method -- update_squares
            Updates the self.squares list of lists after a turn has
                ended with the new positions of each CheckerPiece object
        Parameters:
            self -- the current GameState object
            row -- the row to which the player moved in the current turn
            column -- the column to which the player moved in the current turn
            prior_checker_selected -- the CheckerPiece object which was moved
        Returns:
            Nothing. Updates the list of lists containing the state of
                the game board.
        '''
        prior_checker_selected_position = \
            prior_checker_selected.get_location_in_squares(self.squares)
        self.squares[prior_checker_selected_position.row][
            prior_checker_selected_position.column] = None
        self.squares[row][column] = prior_checker_selected
