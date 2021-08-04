class BoardSquare:
    '''
    Class -- BoardSquare
        Represents a square on the game board
    Attributes:
        row -- the row the square is located in
        column -- the column the square is located in
    Methods:
        __eq__ -- Checks if two BoardSquare objects are equal
        __str__ -- returns a string representation of BoardSquare
        __repr__ -- returns a string representation of BoardSquare
    '''

    def __init__(self, row, column):
        '''
        Constructor -- creates a new instance of BoardSquare
        Parameters:
            self -- the current BoardSquare object
        '''
        self.row = row
        self.column = column

    def __eq__(self, other):
        '''
        Method -- __eq__
            Checks if two objects are equal
        Parameters:
            self -- The current BoardSquare object
            other -- An object to compare self to.
        Returns:
            True if the two objects are equal, False otherwise.
        '''
        if type(self) != type(other):
            return False
        return self.row == other.row and self.column == other.column

    def __str__(self):
        '''
        Method -- __str__
            Returns a string representation of the board square.
        Parameter:
            self -- The current BoardSquare object
        Returns:
            A string representation of the Board Square.
        '''
        return "Row: " + str(self.row) + " Column: " + str(self.column)

    def __repr__(self):
        '''
        Method -- __repr__
            Returns a string representation of the board square.
        Parameter:
            self -- The current BoardSquare object
        Returns:
            A string representation of the Board Square.
        '''
        return self.__str__()
