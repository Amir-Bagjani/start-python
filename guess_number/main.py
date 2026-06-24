import random


def main() -> None:
    print("\n== Guess Number Game! ==")

    secret_number = random.randint(0, 100)
    try_count = 1

    print("Hint", secret_number)

    while True:
        try:
            user_input = int(input("Enter a number between 0 to 100: ").strip())

            if user_input > 100 or user_input < 0:
                print("Wrong number, it should be between 0 to 100.")
                continue

            if secret_number == user_input:
                print(f"Congragulation you got this with {try_count} attempt!")
                user_action = (
                    input("Press Enter to restart the game or q to quit: ")
                    .strip()
                    .lower()
                )
                if user_action == "q":
                    print("Goodbye")
                    break
                else:
                    try_count = 1
                    secret_number = random.randint(0, 100)
                    print("Hint", secret_number)

                    continue
            elif user_input > secret_number:
                try_count += 1
                print("Wrong! you choice is greater than secret number.")
            else:
                try_count += 1
                print("Wrong! you choice is less than secret number.")

        except ValueError:
            print("Only number")
        # generate random number


if __name__ == "__main__":
    main()
