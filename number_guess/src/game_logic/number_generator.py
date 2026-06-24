import random


def generate_random_number(start: int, end: int) -> int:
    """Generate a random number between start and end, include start and end"""
    return random.randint(start, end)
