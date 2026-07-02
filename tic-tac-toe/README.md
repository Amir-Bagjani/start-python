# Tic Tac Toe Game

A simple command-line Tic Tac Toe game written in Python for two players. The game randomly selects which player (`X` or `O`) starts first and continues until a player wins or the game ends in a draw.

## Features

- Two-player gameplay
- Randomly selects the first player
- Displays the game board after every move
- Detects winning conditions
- Detects draw condition
- Alternates turns between players
- Simple command-line interface

## Project Structure

```
tic_tac_toe.py
```

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

1. Clone or download the project.

2. Open a terminal in the project directory.

3. Run:

```bash
python tic_tac_toe.py
```

## Game Board

The board positions are numbered as follows:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Players enter a number between **1** and **9** to place their mark.

## How to Play

1. The game randomly chooses whether **X** or **O** starts.
2. Players take turns entering a cell number.
3. If a player forms three marks in a row, column, or diagonal, they win.
4. If all cells are filled without a winner, the game ends in a draw.

## Example

```
 | |
-----
 | |
-----
 | |

Player X turn
Enter cell number from 1 to 9: 5

 | |
-----
 |X|
-----
 | |

Player O turn
```

## Winning Conditions

A player wins by occupying any of the following:

- Top row
- Middle row
- Bottom row
- Left column
- Middle column
- Right column
- Main diagonal
- Secondary diagonal

## Future Improvements

- Input validation using exception handling
- Prevent crashes on invalid input
- Single-player mode against the computer
- Replay option
- Score tracking
- Colored terminal output
- Graphical User Interface (GUI)