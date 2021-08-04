'''
Shefali Khatri
CS 5001, Fall 2020
This code allows a user to play a game of checkers
with the computer.
'''

# import classes
import turtle
from gamestate import GameState
from checkerpiece import CheckerPiece
from boardsquare import BoardSquare
from computerplayer import ComputerPlayer
from sketch import Sketch

# set constants
NUM_SQUARES = 8  # The number of squares on each row.
SQUARE = 50  # The size of each square in the checkerboard.
BOARD_SIZE = NUM_SQUARES * SQUARE
TOP_CORNER = BOARD_SIZE/2
BOTTOM_CORNER = -BOARD_SIZE/2

# set global variables
sketch = None
game = None
AI = None
valid_squares = None
game_over = False
move_options = None
last_checker_selected = None
last_square = None


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
                of function automatically called by Turtle. This function
                is solely responsible for coordinating the moves on the
                board based on where the user has clicked.
    '''
    # updates board if game is still being played
    if not game_over and (BOTTOM_CORNER <= x <= TOP_CORNER) \
            and (BOTTOM_CORNER <= y <= TOP_CORNER):
        # get row, column, checkerpiece of mouse click
        column = coordinate_to_index(x)
        row = coordinate_to_index(y)
        current_piece = game.piece_selected(row, column)
        valid_pieces = game.get_valid_pieces()

        # if mouse click is on current player's checkerpiece, update board
        if current_piece is not None and current_piece.color == \
                game.current_player and current_piece in valid_pieces:
            update_board_for_selected_piece(row, column, current_piece)

        # if mouse click is on valid empty square, move selected
        # piece to empty square
        else:
            if last_checker_selected is not None:
                update_board_for_player_move(row, column, current_piece)

        # after user has moved piece, AI selects piece and makes move
        while game.current_player == "RED" and game.get_red_count() != 0:
            ai_selected_piece = AI.select_piece(game)
            ai_selected_piece_position = \
                ai_selected_piece.get_location_in_squares(game.squares)
            update_board_for_selected_piece(
                ai_selected_piece_position.row,
                ai_selected_piece_position.column, ai_selected_piece)
            target_location = AI.make_move(ai_selected_piece, game.squares)
            update_board_for_player_move(
                target_location.row, target_location.column, ai_selected_piece)

    # updates board if game is over
    if game_over:
        black_count = game.get_black_count()
        if black_count == 0:
            sketch.draw_game_over("You Lose", "Red")
        else:
            sketch.draw_game_over("You Win!", "Green")


def update_board_for_selected_piece(row, column, selected_piece):
    '''
    Function -- update_board_for_selected_piece
        Unhighlights existing board squares and highlights the possible
            moves for the selected userpiece. Also stores selected checker
            piece and selected board square.
    Parameters:
        row -- the row on the board which contains the selected checker piece
        column -- the column on the board which contains the selected
            checker piece
        selected_piece -- the checkerpiece object the user selected to move
    Returns:
        Nothing. This is only used to store information about
            the selected piece and update the board for the possible
            moves the selected checker piece can make.
    '''
    global move_options
    global last_checker_selected
    global last_square

    sketch.unhighlight_squares(valid_squares)
    sketch.unhighlight_squares(move_options)
    move_options = selected_piece.get_possible_moves(game.squares)
    sketch.highlight_squares("blue", move_options)
    last_checker_selected = selected_piece
    last_square = BoardSquare(row, column)
    return


def update_board_for_player_move(row, column, selected_piece):
    '''
    Function -- update_board_for_player_move
        If the user has selected a valid board square, the checker
            piece is moved to the board square. If a capture is made in
            the process, the opponents piece is removed from the board.
    Parameters:
        row -- the row containing the board square the player wants to
            move their checker piece to
        column -- the column containing the board square the player wants
            to move their checker piece to
        selected_piece -- the checker piece the user selected in their
            previous click
    Returns:
        Nothing. This is only used to update the board for the move the
            user would like to make, whether it is a capture move or not.
    '''

    global valid_squares
    global game_over

    current_square = BoardSquare(row, column)

    # if selected move is a valid move, unhighlight options
    if current_square in move_options:
        sketch.unhighlight_squares(move_options)

        # update board for capture move
        if last_checker_selected.can_capture(game.squares):
            jumped_square = last_checker_selected.get_jumped_square(
                current_square, last_square)
            sketch.update_board_for_capture(row, column,
                                            last_checker_selected,
                                            jumped_square, game)
            game_over = game.end_capture_move(last_checker_selected,
                                              jumped_square)

        # update board for normal move
        else:
            sketch.update_board_for_move(row, column,
                                         last_checker_selected, game)
            game_over = game.end_move()

        # setup board for next move by highlighting valid squares
        valid_squares = game.get_valid_squares()
        sketch.highlight_squares("red", valid_squares)
        move_options.clear()
    return


def coordinate_to_index(coordinate):
    '''
        Function -- coordinate_to_index
            Takes a coordinate and converts it to the corresponding
                row or column
        Parameters:
            Coordinate - represents an x or y coordinate where a
                user may have clicked
        Returns:
            The equivalent row or column that corresponds to the coordinate
    '''
    NORMALIZATION_FACTOR = 200
    return int((coordinate + NORMALIZATION_FACTOR)//SQUARE)


def main():
    global sketch
    global game
    global AI
    # global last_checker_selected
    global valid_squares

    # draw board
    sketch = Sketch()
    sketch.draw_checkerboard()
    sketch.draw_checkerpieces()

    # set up game and computer player
    game = GameState()
    AI = ComputerPlayer()
    # last_checker_selected = None

    # highlight valid pieces for initial move
    valid_squares = game.get_valid_squares()
    sketch.highlight_squares("red", valid_squares)

    # Start Click handling
    sketch.setup_click_handling(click_handler)


if __name__ == "__main__":
    main()
