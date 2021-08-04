from gamestate import GameState
from checkerpiece import CheckerPiece
from boardsquare import BoardSquare


def test_constructor():
    checkerpiece = CheckerPiece("BLACK")
    assert(checkerpiece.color == "BLACK")
    assert(checkerpiece.is_king is False)
    assert(checkerpiece.can_move_forward)
    assert(checkerpiece.can_move_back is False)


def test_get_location_in_squares():
    game = GameState()
    piece_in_game = game.piece_selected(2, 1)
    piece_location = piece_in_game.get_location_in_squares(game.squares)
    assert(piece_location.row == 2)
    assert(piece_location.column == 1)


def test_get_possible_moves():
    game = GameState()
    piece_in_game = game.piece_selected(2, 1)
    assert(piece_in_game.get_possible_moves(
        game.squares) == [BoardSquare(3, 0), BoardSquare(3, 2)])
    game.update_squares(4, 1, game.piece_selected(2, 3))
    piece_in_game2 = game.piece_selected(5, 0)
    assert(piece_in_game2.get_possible_moves(
        game.squares) == [BoardSquare(3, 2)])


def test_can_capture():
    game = GameState()
    game.update_squares(4, 1, game.piece_selected(2, 3))
    piece_in_game = game.piece_selected(5, 0)
    assert(piece_in_game.can_capture(game.squares))
    piece_in_game2 = game.piece_selected(1, 0)
    assert(piece_in_game2.can_capture(game.squares) is False)


def test_get_capturing_moves():
    game = GameState()
    game.update_squares(4, 1, game.piece_selected(2, 3))
    piece_in_game = game.piece_selected(5, 0)
    assert(piece_in_game.get_capturing_moves(
        game.squares) == [BoardSquare(3, 2)])
    piece_in_game2 = game.piece_selected(2, 5)
    assert(piece_in_game2.get_capturing_moves(game.squares) == [])


def test_get_non_capturing_moves():
    game = GameState()
    piece_in_game = game.piece_selected(1, 2)
    assert(piece_in_game.get_non_capturing_moves(game.squares) == [])
    piece_in_game2 = game.piece_selected(2, 3)
    assert(piece_in_game2.get_non_capturing_moves(
        game.squares) == [BoardSquare(3, 2), BoardSquare(3, 4)])
    piece_in_game3 = game.piece_selected(5, 0)
    assert(piece_in_game3.get_non_capturing_moves(
        game.squares) == [BoardSquare(4, 1)])


def test_get_legal_non_capturing_moves():
    game = GameState()
    game_piece = game.piece_selected(2, 3)
    assert(game_piece.get_legal_non_capturing_moves(
        [BoardSquare(3, 2), BoardSquare(3, 4)], game.squares) ==
        [BoardSquare(3, 2), BoardSquare(3, 4)])
    game_piece2 = game.piece_selected(1, 0)
    assert(game_piece2.get_legal_non_capturing_moves(
        [BoardSquare(2, -1), BoardSquare(2, 1)], game.squares) == [])
    game_piece3 = game.piece_selected(5, 0)
    assert(game_piece3.get_legal_non_capturing_moves(
        [BoardSquare(4, -1), BoardSquare(4, 1)], game.squares) ==
        [BoardSquare(4, 1)])
    game_piece4 = game.piece_selected(7, 6)
    assert(game_piece4.get_legal_non_capturing_moves(
        [BoardSquare(6, 5), BoardSquare(6, 7)], game.squares) == [])


def test_get_legal_capturing_moves():
    game = GameState()
    game_piece = game.piece_selected(2, 3)
    assert(game_piece.get_legal_capturing_moves(
            BoardSquare(2, 3), [BoardSquare(4, 1), BoardSquare(4, 5)],
            game.squares) == [])
    game.update_squares(3, 2, game.piece_selected(5, 0))
    assert(game_piece.get_legal_capturing_moves(
            BoardSquare(2, 3), [BoardSquare(4, 1), BoardSquare(4, 5)],
            game.squares) == [BoardSquare(4, 1)])
    game_piece2 = game.piece_selected(5, 6)
    assert(game_piece2.get_legal_capturing_moves(
            BoardSquare(5, 6), [BoardSquare(3, 4), BoardSquare(3, 8)],
            game.squares) == [])


def test_get_jumped_square():
    game = GameState()
    piece = game.piece_selected(2, 3)
    start = BoardSquare(2, 3)
    end = BoardSquare(4, 1)
    jumped_square = piece.get_jumped_square(end, start)
    assert(jumped_square.row == 3)
    assert(jumped_square.column == 2)


def test_end_turn():
    game = GameState()
    game_piece_black = game.piece_selected(2, 3)
    assert(game_piece_black.color == "BLACK")
    assert(game_piece_black.is_king is False)
    assert(game_piece_black.can_move_back is False)
    assert(game_piece_black.can_move_forward)
    game.update_squares(7, 2, game_piece_black)
    game_piece_black.end_turn(game.squares)
    assert(game_piece_black.color == "BLACK")
    assert(game_piece_black.is_king)
    assert(game_piece_black.can_move_back)
    assert(game_piece_black.can_move_forward)
    game_piece_red = game.piece_selected(5, 0)
    assert(game_piece_red.color == "RED")
    assert(game_piece_red.is_king is False)
    assert(game_piece_red.can_move_back)
    assert(game_piece_red.can_move_forward is False)
    game.update_squares(0, 1, game_piece_red)
    game_piece_red.end_turn(game.squares)
    assert(game_piece_red.color == "RED")
    assert(game_piece_red.is_king)
    assert(game_piece_red.can_move_back)
    assert(game_piece_red.can_move_forward)
