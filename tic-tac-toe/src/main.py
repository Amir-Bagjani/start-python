import random


class TicTacToe:
    """
    A command-line implementation of the Tic Tac Toe game.

    The game supports two human players who take turns placing
    their marks ('X' or 'O') on a 3×3 board. The starting player
    is selected randomly. The game continues until one player wins
    or the board is completely filled, resulting in a draw.

    Attributes
    ----------
    board : list
        A list representing the game board.
        Index 0 is unused, while indices 1-9 represent
        the nine cells of the board.

    player_turn : str
        The symbol ('X' or 'O') of the current player.
    """

    def __init__(self):
        """
        Initializes a new Tic Tac Toe game.

        Creates an empty game board and randomly selects
        the player who will make the first move.
        """
        self.board = [" "] * 10  # index zero is not used
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self):
        """
        Randomly selects the player who starts the game.

        Returns
        -------
        str
            Either 'X' or 'O'.
        """
        return random.choice(["X", "O"])

    def show_board(self):
        """
        Displays the current state of the game board
        in a 3×3 grid format.

        Returns
        -------
        None
        """
        print("\n")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-----")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-----")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])

    def swap_player_turn(self):
        """
        Switches the current player.

        If the current player is 'X', it changes to 'O',
        and vice versa.

        Returns
        -------
        str
            The updated player's symbol.
        """
        self.player_turn = "X" if self.player_turn == "O" else "O"
        return self.player_turn

    def is_board_filled(self):
        """
        Checks whether all cells on the board have been occupied.

        Returns
        -------
        bool
            True if the board is full.
            False otherwise.
        """
        return " " not in self.board[1:]

    def fix_spot(self, cell, player):
        """
        Places the player's mark on the selected board position.

        Parameters
        ----------
        cell : int
            Board position (1-9).

        player : str
            Player symbol ('X' or 'O').

        Returns
        -------
        None
        """
        self.board[cell] = player

    def has_player_won(self, player):
        """
        Determines whether the specified player has won the game.

        The method checks all possible winning combinations
        (rows, columns, and diagonals).

        Parameters
        ----------
        player : str
            Player symbol ('X' or 'O').

        Returns
        -------
        bool
            True if the player has a winning combination.
            False otherwise.
        """
        win_combination = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]
        for combination in win_combination:
            win = []
            for cell in combination:
                win.append(self.board[cell] == player)

            if False not in win:
                return True

        return False

    def start(self):
        """
        Starts the Tic Tac Toe game.

        The game repeatedly:
        - Displays the board.
        - Prompts the current player for a move.
        - Validates the move.
        - Updates the board.
        - Checks for a winner.
        - Checks for a draw.
        - Switches turns if the game continues.

        The loop terminates when a player wins or the game ends in a draw.

        Returns
        -------
        None
        """
        while True:
            self.show_board()
            print(f"Player {self.player_turn} turn")
            cell = int(input("Enter cell number from 1 to 9: "))

            if self.board[cell] == " " and cell in range(1, 10):
                self.fix_spot(cell, self.player_turn)

                if self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f"Player {self.player_turn} won")
                    break

                if self.is_board_filled():
                    print("Draw!")
                    break

                self.swap_player_turn()
            else:
                print("Invalid cell numbe")


def main():
    """
    Creates a TicTacToe object and starts the game.

    This function serves as the entry point of the application.

    Returns
    -------
    None
    """
    game = TicTacToe()
    game.start()


if __name__ == "__main__":
    main()
