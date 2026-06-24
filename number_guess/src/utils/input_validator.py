def get_valid_input(start: int, end: int) -> int:
    while True:
        try:
            user_input = int(input("Enter a number: ").strip())
            if start <= user_input <= end:
                return user_input
            else:
                print(f"Wrong input. Please wnter a number between {start} nad {end}.")
                continue
        except ValueError:
            print("Wront input, Please enter a number.")
            continue


if __name__ == "__main__":
    print(get_valid_input(1, 50))
