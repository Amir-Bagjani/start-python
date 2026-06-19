from utils.check_for_zero_division import check_for_zero_division


def divide(n1: float, n2: float) -> float:
    check_for_zero_division(n2)
    return n1 / n2
