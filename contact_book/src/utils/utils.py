def show_menu():
    """
    Display the application's main menu.

    Returns:
        None.
    """
    print("\nWelcome to contact book application!")
    print("1. Add contact")
    print("2. Edit contact")
    print("3. View contacts")
    print("4. Delete contact")
    print("5. Show menu")
    print("6. Quit")


def get_user_choice(prompt: str, required: bool = False):
    """
    Prompt the user for input.

    The user may enter 'q' to cancel the operation. If the input is required,
    the prompt is repeated until a non-empty value is entered or the user
    cancels.

    Args:
        prompt: The message displayed to the user.
        required: Whether a non-empty value is required.

    Returns:
        The user's input as a string, an empty string for optional blank input,
        or None if the user enters 'q'.
    """
    while True:
        user_choice = input(prompt).strip()

        if user_choice == "q":
            return None

        if (not user_choice) and required:
            print("Wrong!! this field is required")
            continue

        return user_choice
