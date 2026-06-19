def get_todo_id(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid id.")


def get_todo_title(propmt: str) -> str:
    while True:
        title = input(propmt).strip()
        if title:
            return title

        print("Title cannot be Empty.")
