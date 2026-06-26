import nltk
import random
import string
from abc import ABC, abstractmethod

nltk.download("words")


class PasswordGenerator(ABC):

    @abstractmethod
    def generate(self) -> str:
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length

    def generate(self):
        return "".join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(
        self, length: int, includes_number: bool = False, includes_symbol: bool = False
    ):
        self.length = length
        self.choices = string.ascii_letters
        if includes_symbol:
            self.choices += string.punctuation
        if includes_number:
            self.choices += string.digits

    def generate(self):
        return "".join([random.choice(self.choices) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self, words_number: int, separator: str = "-", capitalize: bool = False
    ):
        self.slected_separator = separator
        self.words_number = words_number
        self.capitalize = capitalize
        # self.separator_options = ("-", ".", "/", ";")

    def generate(self):
        choices = nltk.corpus.words.words()

        words = [random.choice(choices) for _ in range(self.words_number)]

        if self.capitalize:
            words = [word.capitalize() for word in words]

        return self.slected_separator.join(words)


def test_pin():
    pin_generator = PinGenerator(8)
    password = pin_generator.generate()
    print(password)
    assert len(password) == 8
    assert all(char in string.digits for char in password)


def test_random():
    random_generator = RandomPasswordGenerator(
        length=12, includes_symbol=True, includes_number=True
    )
    password = random_generator.generate()
    print(password)

    allowed = string.ascii_letters + string.digits + string.punctuation

    assert len(password) == 12
    assert all(c in allowed for c in password)


def memorable_random():
    memorable_generator = MemorablePasswordGenerator(
        words_number=5, separator="*", capitalize=True
    )
    password = memorable_generator.generate()
    print(password)

    assert len(password.split("*")) == 5
    assert all(char[0].istitle() for char in password.split("*"))


def main():
    print("Testing pincode generator:")
    test_pin()

    print("Testing random password generator:")
    test_random()

    print("Testing memorable password generator:")
    memorable_random()


if __name__ == "__main__":
    main()
