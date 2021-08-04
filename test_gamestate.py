from gamestate import GameState
from checkerpiece import CheckerPiece
from boardsquare import BoardSquare


def test_constructor():
    game = GameState()
    squares = [[None, game.piece_selected(0, 1), None,
                game.piece_selected(0, 3), None,
                game.piece_selected(0, 5), None,
                game.piece_selected(0, 7)],
               [game.piece_selected(1, 0), None,
                game.piece_selected(1, 2), None,
                game.piece_selected(1, 4), None,
                game.piece_selected(1, 6), None],
               [None, game.piece_selected(2, 1), None,
                game.piece_selected(2, 3), None,
                game.piece_selected(2, 5),
                None, game.piece_selected(2, 7)],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [game.piece_selected(5, 0), None,
                game.piece_selected(5, 2), None,
                game.piece_selected(5, 4), None,
                game.piece_selected(5, 6), None],
               [None, game.piece_selected(6, 1), None,
                game.piece_selected(6, 3), None,
                game.piece_selected(6, 5), None, game.piece_selected(6, 7)],
               [game.piece_selected(7, 0), None, game.piece_selected(7, 2),
                None, game.piece_selected(7, 4), None,
                game.piece_selected(7, 6), None]]
    assert(game.squares == squares)
    assert(game.current_player == "BLACK")
    assert(game.red_count == 12)
    assert(game.black_count == 12)


def test_piece_selected():
    game = GameState()
    assert(game.piece_selected(4, 7) is None)
    assert(game.piece_selected(0, 1).color == "BLACK")
    assert(game.piece_selected(0, 1).is_king is False)
    assert(game.piece_selected(7, 0).color == "RED")
    assert(game.piece_selected(7, 0).is_king is False)


def test_get_valid_pieces():
    game = GameState()
    assert(game.get_valid_pieces() ==
           [game.piece_selected(2, 1), game.piece_selected(2, 3),
           game.piece_selected(2, 5), game.piece_selected(2, 7)])
    game.update_squares(3, 2, game.piece_selected(5, 0))
    assert(game.get_valid_pieces() ==
           [game.piece_selected(2, 1), game.piece_selected(2, 3)])


def test_get_valid_squares():
    game = GameState()
    assert(game.get_valid_squares() ==
           [BoardSquare(2, 1), BoardSquare(2, 3),
           BoardSquare(2, 5), BoardSquare(2, 7)])
    game.end_move()
    assert(game.get_valid_squares() ==
           [BoardSquare(5, 0), BoardSquare(5, 2),
           BoardSquare(5, 4), BoardSquare(5, 6)])
    game.update_squares(3, 2, game.piece_selected(5, 2))
    game.end_move()
    assert(game.get_valid_squares() == [BoardSquare(2, 1), BoardSquare(2, 3)])


def test_get_black_count():
    game = GameState()
    assert(game.get_black_count() == 12)
    game.end_capture_move(game.piece_selected(5, 0), BoardSquare(2, 1))
    assert(game.get_black_count() == 11)


def test_get_red_count():
    game = GameState()
    assert(game.get_red_count() == 12)
    game.end_capture_move(game.piece_selected(2, 1), BoardSquare(5, 0))
    assert(game.get_red_count() == 11)


def test_end_move():
    print("opening method")
    game = GameState()
    assert(game.current_player == "BLACK")
    game.end_move()
    assert(game.current_player == "RED")
    assert(game.end_move() is False)
    # remove all Black pieces on game board
    game.end_move()
    game.end_capture_move(game.piece_selected(7, 0), BoardSquare(0, 1))
    game.end_capture_move(game.piece_selected(7, 2), BoardSquare(0, 3))
    game.end_capture_move(game.piece_selected(7, 4), BoardSquare(0, 5))
    game.end_capture_move(game.piece_selected(7, 6), BoardSquare(0, 7))
    game.end_capture_move(game.piece_selected(6, 1), BoardSquare(1, 0))
    game.end_capture_move(game.piece_selected(6, 3), BoardSquare(1, 2))
    game.end_capture_move(game.piece_selected(6, 5), BoardSquare(1, 4))
    game.end_capture_move(game.piece_selected(6, 7), BoardSquare(1, 6))
    game.end_capture_move(game.piece_selected(5, 0), BoardSquare(2, 1))
    game.end_capture_move(game.piece_selected(5, 2), BoardSquare(2, 3))
    game.end_capture_move(game.piece_selected(5, 4), BoardSquare(2, 5))
    game.end_capture_move(game.piece_selected(5, 6), BoardSquare(2, 7))
    assert(game.end_move() is True)


def test_end_capture_move():
    game = GameState()
    assert(game.end_capture_move(
        game.piece_selected(2, 1), BoardSquare(5, 0)) is False)
    assert(game.squares[5][0] is None)
    assert(game.get_red_count() == 11)
    # remove all but one black piece
    game.end_capture_move(game.piece_selected(7, 0), BoardSquare(0, 1))
    game.end_capture_move(game.piece_selected(7, 2), BoardSquare(0, 3))
    game.end_capture_move(game.piece_selected(7, 4), BoardSquare(0, 5))
    game.end_capture_move(game.piece_selected(7, 6), BoardSquare(0, 7))
    game.end_capture_move(game.piece_selected(6, 1), BoardSquare(1, 0))
    game.end_capture_move(game.piece_selected(6, 3), BoardSquare(1, 2))
    game.end_capture_move(game.piece_selected(6, 5), BoardSquare(1, 4))
    game.end_capture_move(game.piece_selected(6, 7), BoardSquare(1, 6))
    game.end_capture_move(game.piece_selected(6, 7), BoardSquare(2, 1))
    game.end_capture_move(game.piece_selected(5, 2), BoardSquare(2, 3))
    game.end_capture_move(game.piece_selected(5, 4), BoardSquare(2, 5))
    print("testing: " + str(game.get_black_count()))
    assert(game.end_capture_move(
        game.piece_selected(5, 6), BoardSquare(2, 7)) is True)


def test_update_squares():
    game = GameState()
    gamepiece = game.piece_selected(2, 3)
    game.update_squares(3, 4, gamepiece)
    assert(game.piece_selected(3, 4) == gamepiece)
    assert(game.piece_selected(2, 3) is None)
