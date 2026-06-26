import random


class RockPaperScissors:
    """Main class for rock paper scissors game.
    """
    def __init__(self, name: str) -> None:
        self.choices = ("rock", "paper", "scissors")
        self.name = name

    def get_player_name(self) -> str:
        """Get computer choice randomly from choices: rock, paper, scissors.

        Returns:
            str: one of rock, paper or scissors
        """
        return self.name

    def get_user_choice(self) -> str:
        while True:
            user_choice = (
                input("\nChoose one of the: Rock, Paper or Scissors: ").strip().lower()
            )

            if user_choice == "q":
                print("Goodbye!")
                return "q"

            if user_choice not in self.choices:
                print("Wrong choice!")
                continue

            return user_choice

    def print_instructions(self) -> None:
        print("This is Rock paper scissors Game!\n")
        print("You can quit the game with perssing q")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        game_rule = {
            "rock": {"scissors": "win", "paper": "loss", "rock": "draw"},
            "paper": {"rock": "win", "scissors": "loss", "paper": "draw"},
            "scissors": {"paper": "win", "rock": "loss", "scissors": "draw"},
        }

        result = game_rule[user_choice][computer_choice]

        return f"You chose {user_choice} and computer chose {computer_choice}: {result}"

    def play(self):
        user_choice = self.get_user_choice()

        if user_choice == "q":
            return

        computer_choice = self.get_computer_choice()

        print(self.decide_winner(user_choice, computer_choice))


def play_again(name: str) -> bool:
    play_again = (
        input(f"{name} do you want play again press Y and for quit press any key: ")
        .strip()
        .lower()
    )

    return play_again == "y"


def main() -> None:
    game = RockPaperScissors("Amir")
    game.print_instructions()

    while True:
        game.play()

        if not play_again(game.get_player_name()):
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
