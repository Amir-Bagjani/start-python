# Password Generator

A simple Python project that demonstrates object-oriented programming by implementing multiple password generators using an abstract base class.

## Features

This project includes three types of password generators:

- **PIN Generator**
  - Generates a numeric PIN of a specified length.

- **Random Password Generator**
  - Generates a random password using letters.
  - Optionally includes digits.
  - Optionally includes punctuation symbols.

- **Memorable Password Generator**
  - Generates a password made of random English words.
  - Customizable separator.
  - Optional capitalization of each word.

## Project Structure

```text
.
├── main.py
└── README.md
```

## Requirements

- Python 3.8+
- NLTK

## Installation

1. Clone the repository:

```bash
# clone repository
cd password-generator
```

2. Install the required package:

```bash
pip install -r requirements.txt
```

3. The program automatically downloads the NLTK English words corpus the first time it runs:

```python
nltk.download("words")
```

## Usage

Run the program:

```bash
python main.py
```

Example output:

```text
Testing pincode generator:
48193725

Testing random password generator:
g!2hJ8#xM@4Q

Testing memorable password generator:
Apple*Bridge*Mountain*Ocean*Forest
```

## Example

### Generate an 8-digit PIN

```python
pin = PinGenerator(8)
print(pin.generate())
```

### Generate a 12-character random password

```python
password = RandomPasswordGenerator(
    length=12,
    includes_number=True,
    includes_symbol=True,
)

print(password.generate())
```

### Generate a memorable password

```python
password = MemorablePasswordGenerator(
    words_number=5,
    separator="-",
    capitalize=True,
)

print(password.generate())
```

## Testing

The project includes simple test functions:

- `test_pin()`
- `test_random()`
- `memorable_random()`

Run them by executing:

```bash
python password_generator.py
```

## Concepts Demonstrated

- Abstract Base Classes (`abc`)
- Inheritance
- Polymorphism
- Random value generation
- Working with strings
- Using external libraries (NLTK)
- Basic unit testing with assertions

## Notes

- The random password generator allows digits and symbols when enabled, but does **not guarantee** that at least one digit or symbol will appear in every generated password.
- The memorable password generator uses the NLTK English words corpus.

## License

This project is released under the MIT License.