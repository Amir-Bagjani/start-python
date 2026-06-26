number = 45


def happy_number(number: int) -> bool:
    seen_number = set()

    while (number != 1) and (number not in seen_number):
        seen_number.add(number)
        number = sum([int(n) ** 2 for n in str(number)])

    return number == 1


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter number to check if it is happy or not: ").strip())
            happy = happy_number(number)
            print("Yes it is happy." if happy else "No it is not happy.")
            break
        except ValueError:
            print("Wrong number, try a digit!!")
