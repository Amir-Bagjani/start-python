def get_input(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip()

        try:
            return float(user_input)
        except ValueError:
            print("Invalid number. Try again.")
