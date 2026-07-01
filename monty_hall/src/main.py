import random
from typing import Tuple


def monty_hall(switch: bool = False) -> bool:
    """
    Simulate a single Monty Hall game.

    The player randomly selects one of three doors. One door hides a car
    and the other two hide goats. If ``switch`` is True, the player
    switches to the remaining unopened door after Monty reveals a goat.

    Args:
        switch (bool, optional): Whether the player switches their choice.
            Defaults to False.

    Returns:
        bool: True if the player wins the car, otherwise False.
    """

    choices = ["goat", "car", "goat"]
    random.shuffle(choices)

    initial_choice = random.choice(range(3))

    if switch:
        other_choices = [
            i for i in range(3) if i != initial_choice and choices[i] != "car"
        ]
        suggest = random.choice(other_choices)
        final_choice = [i for i in range(3) if i != initial_choice and i != suggest][0]
    else:
        final_choice = initial_choice

    return choices[final_choice] == "car"


def simulate_game(num_games: int) -> Tuple[int, int]:
    """
    Simulate one or more Monty Hall games.

    Args:
        num_games (int): Number of games to simulate.

    Returns:
        tuple[int, int]:
            A tuple containing:
            - wins_without_switch (int): Number of wins when the player does not switch.
            - wins_with_switch (int): Number of wins when the player switches.
    """
    not_switched = sum(monty_hall(False) for _ in range(num_games))
    switched = sum(monty_hall(True) for _ in range(num_games))

    return not_switched, switched


def main():
    print(simulate_game(1000))


if __name__ == "__main__":
    main()
