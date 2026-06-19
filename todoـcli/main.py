from pathlib import Path

from utils.file_handler import load_todo
from services.todo_service import show_todos
from cli.handlers import handle_add, handle_remove, handle_change_status
from cli.show_menu import show_menu

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "todos.json"


def main() -> None:
    todos = load_todo(FILE_PATH)

    while True:
        show_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            handle_add(todos, FILE_PATH)
        elif choice == "2":
            show_todos(todos)
        elif choice == "3":
            handle_remove(todos, FILE_PATH)
        elif choice == "4":
            handle_change_status(todos, FILE_PATH)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
