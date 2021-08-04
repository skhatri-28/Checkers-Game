from random import randint


class ComputerPlayer:
    '''
    Class -- ComputerPlayer
        Represents the Computer player.
    Attributes:
        None
    Methods:
        select_piece -- selects a valid piece to move
        make_move -- indicates the BoardSquare object to move
            the selected piece to
    '''

    def select_piece(self, gamestate):
        '''
        Method -- select_piece
            This function returns a valid checkerpiece object that the
                ComputerPlayer will move.
        Parameters:
            self -- the current ComputerPlayer object
            gamestate -- an object representing the current state of the game
        Returns:
            A checkerpiece object selected by the ComputerPlayer to move.
        '''
        piece_selected = None
        valid_pieces = gamestate.get_valid_pieces()
        if len(valid_pieces) != 0:
            index = randint(0, len(valid_pieces)-1)
            piece_selected = valid_pieces[index]
        return piece_selected

    def make_move(self, checkerpiece, squares):
        '''
        Method -- make_move
            Returns a BoardSquare object given a specific CheckerPiece.
                The BoardSquare object represents a valid location
                the CheckerPiece object can move to on the board.
        Parameters:
            self -- the current ComputerPlayer object
            checkerpiece -- A CheckerPiece object that has been selected
                by the ComputerPlayer.
            squares -- A list of lists representing the state of the game
                board and where each object is place on the board
        Returns:
            A BoardSquare object indicating the location to where
                the selected CheckerPiece object should move.
        '''
        move_choices = None
        move_choices = checkerpiece.get_possible_moves(squares)
        if move_choices != 0:
            index = randint(0, len(move_choices)-1)
            move_selected = move_choices[index]
        return move_selected
