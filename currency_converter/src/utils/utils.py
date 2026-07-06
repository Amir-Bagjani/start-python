from datetime import datetime


def last_update(time: int):
    last = datetime.fromtimestamp(time)
    now = datetime.now()
    delta = now - last
    second = int(delta.total_seconds())

    if second < 60:
        return f"{second} seconds ago."
    elif second < 3600:
        return f"{second // 60} minutes ago."
    elif second < 86400:
        return f"{second // 3600} hours ago."
    else:
        return f"{second // 86400} days ago."


def get_last_update(currency: str):

    return 12750044


def show_menu():
    print("\nWellcome to Currnecy converter")
    print("1. Convert currencies")
    print("2. Exit")


def get_user_choice(prompt: str):
    choice = input(prompt).strip()
    if choice == "q":
        return None
    else:
        return choice


def get_user_amount(prompt: str):
    while True:
        try:
            choice = float(input(prompt).strip())
            if choice == "q":
                return None
            else:
                return choice
        except ValueError:
            print("Wrong amount!!. try again")
