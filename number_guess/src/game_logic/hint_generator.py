def provide_hint(guess: int, actual_number: int) -> None:
    if guess > actual_number:
        print("Your guess is too high.")
    elif guess < actual_number:
        print("Your guess is too low.")
