from boardsquare import BoardSquare


class CheckerPiece:
    '''
    Class -- CheckerPiece
        Represents a Checker Piece on the game board
    Attributes:
        color -- the color of the checker piece
        is_king -- boolean, indicating if the piece is a king or not
        can_move_forward -- boolean, indicating if the piece can move forward
        can_move_backward -- boolean, indicating if the piece can move backward
    Methods:
        get_location_in_squares -- Gets the corresponding BoardSquare
            object for where the CheckerPiece is located
        get_possible_moves -- Gets all possible BoardSquare objects
            the CheckerPiece can move to
        can_capture -- Indicates whether the CheckerPiece can make a
            capturing move or not
        get_capturing_moves -- Gets the BoardSquare objects of all valid
            capturing moves
        get_non_capturing_moves -- Gets the BoardSquare objects of all
            valid non-capturing moves
        get_legal_non_capturing_moves -- Helper method. Identifies legal
            non-capturing moves from a list of non-capturing moves
        get_legal_capturing_moves -- Helper method. Identifies legal
            capturing moves from a list of capturing moves
        get_jumped_square -- Gets the BoardSquare object of a square
            that is jumped over to make a capture
        end_turn -- ends the CheckerPieces turn by updating
            CheckerPieces attributes
    '''

    def __init__(self, color):
        self.color = color
        self.is_king = False
        if self.color == "BLACK":
            self.can_move_forward = True
            self.can_move_back = False
        else:
            self.can_move_forward = False
            self.can_move_back = True

    def get_location_in_squares(self, squares):
        '''
        Method -- get_location_in_squares
            Identifies the current BoardSquare object associated with a given
                CheckerPiece object
        Parameters:
            self -- the current CheckerPiece object
            squares -- list of lists representing the state of the game board
        Returns:
            A BoardSquare object which contains the current CheckerPiece
                object.
        '''
        current_square = None
        MAX_COL_ROW = 8
        for i in range(0, MAX_COL_ROW):
            for j in range(0, MAX_COL_ROW):
                if squares[i][j] == self:
                    current_square = BoardSquare(i, j)
        return current_square

    def get_possible_moves(self, squares):
        '''
        Method -- get_possible_moves
            Gives a list of all possible legal moves for the current
                CheckerPiece object.
        Parameters:
            self -- the current CheckerPiece object
            squares -- list of lists representing the state of the game board
        Returns:
            A list of BoardSquare objects which the current CheckerPiece
                object can legally move to.
        '''
        capturing_moves = self.get_capturing_moves(squares)
        if len(capturing_moves) != 0:
            return capturing_moves
        else:
            return self.get_non_capturing_moves(squares)

    def can_capture(self, squares):
        '''
        Method -- can_capture
            Identifies whether the current CheckerPiece object can
                make a capturing move or not.
        Parameters:
            self -- the current CheckerPiece object
            squares -- list of lists representing the state of the game board
        Returns:
            A boolean indicating whether a capture can be made.
        '''
        move_options = self.get_possible_moves(squares)
        if len(move_options) != 0:
            move_option = move_options[0]
            row = self.get_location_in_squares(squares).row
            return abs(move_option.row - row) == 2
        return False

    def get_capturing_moves(self, squares):
        '''
        Method -- get_capturing moves:
            Identifies all BoardSquare Objects where the current CheckerPiece
                object can move to in order to make a capturing move
        Parameters:
            self -- the current CheckerPiece object
            squares -- list of lists representing the state of the game board
        Returns:
            A list of BoardSquare objects where the current CheckerPiece
                can move to make a capturing move.
        '''
        current_square = self.get_location_in_squares(squares)
        potential_moves = []
        if self.can_move_back:
            back_left = BoardSquare(
                current_square.row - 2, current_square.column - 2)
            back_right = BoardSquare(
                current_square.row - 2, current_square.column + 2)
            potential_moves.append(back_left)
            potential_moves.append(back_right)
        if self.can_move_forward:
            forward_left = BoardSquare(
                current_square.row + 2, current_square.column - 2)
            forward_right = BoardSquare(
                current_square.row + 2, current_square.column + 2)
            potential_moves.append(forward_left)
            potential_moves.append(forward_right)
        move_options = self.get_legal_capturing_moves(
            current_square, potential_moves, squares)
        return move_options

    def get_non_capturing_moves(self, squares):
        '''
        Method -- get_non_capturing_moves
            Identifies all BoardSquare Objects where the current
                CheckerPiece object can move without making a capture.
        Parameters:
            self -- the current CheckerPiece object
            squares -- list of lists representing the state of the game board
        Returns:
            A list of BoardSquare objects where the current CheckerPiece
                can move without making a capture.
        '''
        current_square = self.get_location_in_squares(squares)
        potential_moves = []
        if self.can_move_back:
            back_left = BoardSquare(
                current_square.row - 1, current_square.column - 1)
            back_right = BoardSquare(
                current_square.row - 1, current_square.column + 1)
            potential_moves.append(back_left)
            potential_moves.append(back_right)
        if self.can_move_forward:
            forward_left = BoardSquare(
                current_square.row + 1, current_square.column - 1)
            forward_right = BoardSquare(
                current_square.row + 1, current_square.column + 1)
            potential_moves.append(forward_left)
            potential_moves.append(forward_right)
        move_options = self.get_legal_non_capturing_moves(
            potential_moves, squares)
        return move_options

    def get_legal_non_capturing_moves(self, end_positions, squares):
        '''
        Method -- get_legal_non_capturing_moves
            Given a list of potential non-capturing moves, determines
                whether they are legal.
        Parameters:
            self -- the current CheckerPiece object
            end_positions -- a list of BoardSquare objects indicating the
                CheckerPiece object destinations for potential
                non-capturing moves
            squares - list of lists representing the state of the game board
        Returns:
            A list of BoardSquare objects representing valid non-capturing
                destinations for the current CheckerPiece object.
        '''
        MAX_COL = 7
        MAX_ROW = 7
        legal_moves = []
        for move in end_positions:
            if 0 <= move.row <= MAX_ROW and 0 <= move.column <= MAX_COL:
                if squares[move.row][move.column] is None:
                    legal_moves.append(move)
        return legal_moves

    def get_legal_capturing_moves(
            self, current_square, end_positions, squares):
        '''
        Method -- get_legal_non_capturing_moves
            Given a list of potential capturing moves, determines whether they
                are legal.
        Parameters:
            self -- the current CheckerPiece object
            end_positions -- a list of BoardSquare objects indicating the
                CheckerPiece object destinations for potential capturing moves
            squares - list of lists representing the state of the game board
        Returns:
            A list of BoardSquare objects representing valid capturing
                destinations for the current CheckerPiece object.
        '''
        MAX_ROW = 7
        MAX_COL = 7
        legal_moves = []
        for move in end_positions:
            if 0 <= move.row <= MAX_ROW and 0 <= move.column <= MAX_COL:
                target_is_empty = squares[move.row][move.column] is None
                jumped_square = self.get_jumped_square(move, current_square)
                jumped_piece = squares[jumped_square.row][jumped_square.column]
                # If we jumped over an empty spot, that is not a capturing move
                if jumped_piece is not None:
                    has_jumped_enemy_piece = jumped_piece.color != self.color
                    if target_is_empty and has_jumped_enemy_piece:
                        legal_moves.append(move)
        return legal_moves

    def get_jumped_square(self, end_position, start_position):
        '''
        Method -- get_jumped_square
            Locates the BoardSquare object that is jumped when a capturing
                move is made.
        Parameters:
            self -- the current CheckerPiece object
            end_position -- A BoardSquare object representing the location of
                the CheckerPiece object after a capture is made
            start_position -- A BoardSquare object representing the location of
                the CheckerPiece object before a capture is made
        Returns:
            A BoardSquare object representing the square that was jumped to
                make a capture.
        '''
        row = int((end_position.row + start_position.row)/2)
        col = int((end_position.column + start_position.column)/2)
        return BoardSquare(row, col)

    def end_turn(self, squares):
        '''
        Method -- end_turn
            Ends a CheckerPiece Objects turn and updates object
                attributes if needed
        Parameters:
            self -- the current CheckerPiece object
            squares -- list of lists representing the state of the game board
        Returns:
            Nothing. Updates the object attributes at the end of the
                CheckerPiece's turn.
        '''
        LAST_ROW_BLACK = 7
        LAST_ROW_RED = 0
        if self.color == "BLACK" and\
                self.get_location_in_squares(squares).row == LAST_ROW_BLACK:
            self.is_king = True
            self.can_move_back = True
        if self.color == "RED" and\
                self.get_location_in_squares(squares).row == LAST_ROW_RED:
            self.is_king = True
            self.can_move_forward = True
