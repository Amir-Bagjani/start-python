from custom_operator import divide, floor_divide, modulo
from utils import display_result, get_input, get_operator


class Calculator:
    def __init__(self):
        self.history = []

    def calc(self, num1: float, num2: float, operator: str) -> float:

        operation = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "**": lambda a, b: a**b,
            "/": divide,
            "//": floor_divide,
            "%": modulo,
        }

        op = operation.get(operator)

        if op is None:
            raise ValueError("Unsupported operator.")

        result = op(num1, num2)

        self.history.append(
            {"num1": num1, "num2": num2, "operator": operator, "result": result}
        )

        return result

    def show_history(self) -> None:
        if not self.history:
            print("No history yet!")
            return

        print("\n=== History ===")
        for i, item in enumerate(self.history, 1):
            print(
                f"{i}: {item["num1"]} {item["operator"]} {item["num2"]} = {item["result"]}"
            )


def main() -> None:
    print("=== Calculator ===\n")
    calculator = Calculator()

    while True:
        command = (
            input("\nPress Enter to continue, h to history or q to quit:")
            .strip()
            .lower()
        )
        if command == "q":
            print("Goodbye!")
            break

        if command == "h":
            calculator.show_history()
            continue

        number1 = get_input("Enter first number: ")
        operator = get_operator()
        number2 = get_input("Enter second number: ")

        try:
            display_result(calculator.calc(number1, number2, operator))
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()
