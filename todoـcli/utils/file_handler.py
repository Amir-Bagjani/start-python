import json
from json import JSONDecodeError
from pathlib import Path
from models.todo import Todo


def load_todo(file_path: Path) -> list[Todo]:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return [Todo.from_dict(t) for t in data]
    except (FileNotFoundError, JSONDecodeError):
        return []


def save_todo(todos: list[Todo], file_path: Path) -> None:
    with open(file_path, "w") as file:
        json.dump([todo.to_dict() for todo in todos], file, indent=4)
