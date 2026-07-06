from src.utils.utils import show_menu
from src.handler.currency import convert_handler


def main():
    show_menu()
    while True:
        select_choice = input("\nPlease choose an option(3 for show menu): ").strip()

        if select_choice == "3":
            show_menu()
        elif select_choice == "2":
            print("Goodbye")
            break
        elif select_choice == "1":
            action = convert_handler()
            if action == "break":
                break


if __name__ == "__main__":
    main()
