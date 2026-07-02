from src.model.contact import ContactBook
from src.utils.utils import show_menu
from src.services.services import delete_service, update_service, add_service


def main():
    show_menu()
    book = ContactBook()

    while True:
        user_choice = input("\nPlease choose an option (5 to show menu): ").strip()

        if user_choice == "6":
            print("Goodbye")
            break
        elif user_choice == "5":
            show_menu()
        elif user_choice == "4":
            delete_service(book)
        elif user_choice == "3":
            book.show_contacts()
        elif user_choice == "2":
            if update_service(book) == "continue":
                continue
        elif user_choice == "1":
            if add_service(book) == "continue":
                continue


if __name__ == "__main__":
    main()
