import random


def validate_input(user_input):
    if not user_input.isdigit():
        print("Invalid input please try again.")
        return False

    user_input = int(user_input)
    if user_input > 100 or user_input < 1:
        print("Your guess is wront, it should be between 1 and 100.")
        return False

    return True


def main():
    rand_num = random.randint(0, 100)
    score = 100
    print(rand_num)

    while True:
        user_guess = input("Guess a number between 1 and 100: ").strip()

        if user_guess == "q":
            print("Goodbye!")
            break

        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)

        print(user_guess)

        if user_guess > rand_num:
            print("your guess is too large, try again.")
        elif user_guess < rand_num:
            print("your guess is too low, try again.")
        else:
            print("Congratulation!")
            print("your score is: ", score)
            play_again = input("If you want play again press Enter if not press any key:").strip().lower()
            if play_again == "":
                score = 100
                rand_num = random.randint(1, 100)
                continue
            break

        score -= 10
        score = max(0, score)



if __name__ == "__main__":
    main()
