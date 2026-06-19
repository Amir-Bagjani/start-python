def check_for_zero_division(number):
    if number == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
