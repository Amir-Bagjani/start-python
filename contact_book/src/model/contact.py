from prettytable import PrettyTable

from typing import TypedDict, NotRequired


class ContactData(TypedDict):
    phone: str
    email: NotRequired[str]




class ContactBook:
    """A simple in-memory contact book for storing and managing contacts."""

    def __init__(self):
        """Initialize an empty contact book."""
        self.contacts: dict[str, ContactData] = {}

    def add_contact(self, name: str, phone: str, email: str | None = None):
        """
        Add a new contact to the contact book.

        Args:
            name: The contact's name.
            phone: The contact's phone number.
            email: The contact's email address. Optional.

        Returns:
            None.
        """
        if name in self.contacts:
            print("Contract Already Exists!")
            return

        data: ContactData = {"phone": phone}
        if email:
            data["email"] = email

        self.contacts[name] = data

    def update_contact(
        self,
        contact_name: str,
        phone: str | None = None,
        email: str | None = None,
        name: str | None = None,
    ):
        """
        Update an existing contact's information.

        Args:
            contact_name: The name of the contact to update.
            phone: New phone number. If None, the phone number is unchanged.
            email: New email address. If None, the email is unchanged.
            name: New name for the contact. If None, the name is unchanged.

        Returns:
            None.
        """
        if contact_name not in self.contacts:
            print("Not found!")
            return

        if phone is not None:
            self.contacts[contact_name]["phone"] = phone
        if email is not None:
            self.contacts[contact_name]["email"] = email
        if name is not None:
            self.contacts[name] = self.contacts[contact_name]
            del self.contacts[contact_name]

    def delete_contact(self, contact_name: str):
        """
        Delete a contact from the contact book.

        Args:
            contact_name: The name of the contact to delete.

        Returns:
            None.
        """
        if contact_name not in self.contacts:
            print("Not found!")
            return

        del self.contacts[contact_name]
        print("Contact deleted.")

    def show_contacts(self):
        """
        Display all contacts in the contact book.

        Returns:
            None.
        """
        table = PrettyTable()
        
        if not len(self.contacts):
            print("\nContact list is Empty!")
            return

        table.field_names = ["Name", "Phone number", "Email"]

        for k, v in self.contacts.items():
            table.add_row([k, v["phone"], v.get("email", "")])

        print(table)
