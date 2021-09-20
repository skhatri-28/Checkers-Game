# Checkers Game - Readme

## About The Project

This project allows a user to play the game checkers with a computer opponent. The game is set up on a 8x8 checkerboard with Black and Red checkers. The computer opponent's color is Red and the user's color is Black. Checkerboard squares are highlighted in red for pieces that can be moved at each turn and possible moves for a given piece are highlighted in blue.

### Checkers Rules

1. Player's take turns. The goal of the game is to capture all of the opponent's checker pieces.
2. Pieces may only be moved onto gray squares.
3. Pieces may only be moved forward and diagonally with the exception of King pieces which will be indicated by a checker piece with a gold colored 'K.' King pieces may move in any direction, but must move diagonally. The forward direction is different for both opponents.
3. If a non-capturing move is made, a Checker piece can only move forward one square diagonally.
4. If a capturing move is possible, it must be made. A capturing move is a move in which the current player can diagonally jump over one of the opponent's pieces and land on a gray square. If a capturing move is made, the captured checker will be removed from the board. It is also possible to make multiple jumps in one turn if each opponent's piece is separated by a gray square diagonally.
5. When a checker piece has reached the last row of the board and can no longer go forward, the piece is crowned a King, indicated by a gold colored 'K.' The king pieces may move diagonally in any direction.
6. The game ends when all of the red pieces or black pieces have been captured. If all of the black pieces have been captured, then the user wins. If all of the red pieces have been captured, then the computer wins.


### Built With

The project was built using Python and a pre-installed Python library, Turtle Graphics, for producing a user interface. 

## Usage

### Prerequisites

- Python 3.7.4 or higher
- Turtle Graphics (pre-installed with Python)

### Getting Started

```sh
python {Path to project}\main.py
```
For example:
```sh
python C:\Documents\Checkers\main.py
```

Alternatively, the game can be started by downloading all of the python code into an IDE and running the code from the class main.py.
