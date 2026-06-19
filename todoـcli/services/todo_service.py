from models.todo import Todo


def add_todo(todos: list[Todo], title: str) -> None:
    id = 1
    if todos:
        id = max(t.id for t in todos) + 1

    todos.append(Todo(id, title))


def remove_todo(todos: list[Todo], id: int) -> bool:
    for t in todos:
        if t.id == id:
            todos.remove(t)
            return True

    return False


def change_status_todo(todos: list[Todo], id: int) -> bool:
    for t in todos:
        if t.id == id:
            t.mark_completed() if not t.completed else t.mark_incompleted()
            return True

    return False


def show_todos(todos: list[Todo]) -> None:
    if not todos:
        print("No todos found.")
        return

    print("\n=== Todos ===")
    for t in todos:
        print(t)
