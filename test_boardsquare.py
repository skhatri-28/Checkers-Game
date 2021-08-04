from boardsquare import BoardSquare


def test_constructor():
    square = BoardSquare(4, 7)
    assert(square.row == 4)
    assert(square.column == 7)


def test_eq():
    square1 = BoardSquare(4, 7)
    square2 = BoardSquare(2, 3)
    string = "to compare types"
    assert(square1 != square2)
    assert(square2 == BoardSquare(2, 3))
    assert(square2 != string)


def test_str():
    square1 = BoardSquare(4, 7)
    assert(str(square1) == "Row: 4 Column: 7")


def test_repr():
    square1 = BoardSquare(3, 5)
    assert(repr(square1) == "Row: 3 Column: 5")
