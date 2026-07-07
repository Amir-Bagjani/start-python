from src.constants import SCALES, TENS, UNDER_20


def number_to_word(n: int) -> str:
    """
    Convert a non-negative integer to its English word representation.

    The function supports numbers recursively by breaking them into
    groups such as hundreds, thousands, millions, and larger scales.

    Args:
        n: A non-negative integer to convert.

    Returns:
        The English word representation of `n`.

    Raises:
        ValueError:
            If `n` is negative.

    Examples:
        >>> number_to_word(0)
        'zero'

        >>> number_to_word(7)
        'seven'

        >>> number_to_word(13)
        'thirteen'

        >>> number_to_word(20)
        'twenty'

        >>> number_to_word(42)
        'forty two'

        >>> number_to_word(100)
        'one hundred'

        >>> number_to_word(105)
        'one hundred five'

        >>> number_to_word(342)
        'three hundred forty two'

        >>> number_to_word(1_000)
        'one thousand'

        >>> number_to_word(12_345)
        'twelve thousand three hundred forty five'

        >>> number_to_word(1_000_001)
        'one million one'
    """
    if n < 20:
        return UNDER_20[n]
    elif n < 100:
        remainder = n % 10
        return f"{TENS[n//10]} {UNDER_20[remainder] if remainder != 0 else ''}"
    else:
        pivot = max(k for k in SCALES if k <= n)
        remainder = n % pivot
        return (
            f"{number_to_word(n // pivot)} "
            f"{SCALES[pivot]} "
            f"{number_to_word(remainder) if remainder != 0 else ''}"
        ).strip()


def main():
    print(number_to_word(28))
    print(number_to_word(1_000_001))


if __name__ == "__main__":
    main()
