from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.score import Score
from src.game_logic.hint_generator import provide_hint


def main():
    score = Score(100)
    random_number = generate_random_number(1, 100)

    while True:
        user_input = get_valid_input(1, 100)

        if user_input == random_number:
            print("Correct!")
            print(f"your score is {score.get_score()}")
            break
        else:
            score.decreas(10)
            provide_hint(user_input, random_number)


if __name__ == "__main__":
    main()
