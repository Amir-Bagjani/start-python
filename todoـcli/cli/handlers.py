from pathlib import Path

from models.todo import Todo
from cli.get_user_input import get_todo_id, get_todo_title
from services.todo_service import add_todo, change_status_todo, remove_todo, show_todos
from utils.file_handler import load_todo, save_todo


def handle_add(todos: list[Todo], file_path: Path) -> None:
    title = get_todo_title("Enter Todo title: ")
    add_todo(todos, title)
    save_todo(todos, file_path)

    print("Todo added successfully.")


def handle_remove(todos: list[Todo], file_path: Path) -> None:
    try:
        id = get_todo_id("Enter todo id to remove: ")
        removed = remove_todo(todos, id)
        if removed:
            save_todo(todos, file_path)
            print("Todo removed successfully")
        else:
            print("Todo not found")
    except ValueError:
        print("Todo not found.")

def handle_change_status(todos: list[Todo], file_path: Path) -> None:
    try:
        id = get_todo_id("Enter todo id to change status: ")
        changed = change_status_todo(todos, id)
        if changed:
            save_todo(todos, file_path)
            print("Todo status changed successfully.")
        else:
            print("Todo not found.")
    except ValueError:
        print("Todo not found.")
