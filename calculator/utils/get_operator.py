def get_operator() -> str:
    valid_operators = {"+", "-", "/", "*", "%", "//", "**"}

    while True:
        user_operator = input("Enter operator (+, -, /, *, %, //, **): ").strip()

        if user_operator in valid_operators:
            return user_operator

        print("Invalid operator. Try again.")

