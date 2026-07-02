from src.utils.utils import get_user_choice
from src.model.contact import ContactBook


def delete_service(book: ContactBook):
    """
    Prompt the user for a contact name and delete the contact if provided.

    Args:
        book: The contact book instance.

    Returns:
        None.
    """
    remove_name = get_user_choice("\nEnter the name of contact to delete: ")
    if remove_name:
        book.delete_contact(remove_name)


def update_service(book: ContactBook):
    """
    Prompt the user for updated contact information and apply the changes.

    The user can skip updating individual fields by entering 'n' or cancel
    the operation when prompted for the contact name.

    Args:
        book: The contact book instance.

    Returns:
        "continue" if the operation is canceled; otherwise None.
    """
    update_name = get_user_choice(
        "\nEnter the contact name you want to update: ", required=True
    )
    if update_name is None:
        return "continue"
    new_name = get_user_choice(
        "\nEnter name if you want to update (if not press 'n'): "
    )
    new_phone = get_user_choice(
        "\nEnter phone if you want to update (if not press 'n'): "
    )
    new_email = get_user_choice(
        "\nEnter email if you want to update (if not press 'n'): "
    )

    kwargs = {}

    if new_name != "n":
        kwargs["name"] = new_name
    if new_phone != "n":
        kwargs["phone"] = new_phone
    if new_email != "n":
        kwargs["email"] = new_email

    book.update_contact(contact_name=update_name, **kwargs)


def add_service(book: ContactBook):
    """
    Prompt the user for contact information and add a new contact.

    The operation is canceled if the user quits while entering a required
    field.

    Args:
        book: The contact book instance.

    Returns:
        "continue" if the operation is canceled; otherwise None.
    """
    name = get_user_choice("Please enter a name or press 'q' to quit: ", required=True)
    if name is None:
        return "continue"

    phone = get_user_choice(
        "Please enter a phone number or press 'q' to quit: ", required=True
    )
    if phone is None:
        return "continue"

    email = get_user_choice(
        "Please enter an email number, it is not required: ", required=True
    )

    book.add_contact(name, phone, email)
