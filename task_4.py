
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return """This contact already exists in the phone book.
        "If you need to change the phone number of the contact, use the 'change' command."""


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Name not found!"


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{contacts[name]}"
    else:
        return "Name not found!"


def show_all(contacts):
    if any(contacts):
        return f"{contacts}"
    else:
        return "Contact book is empty!"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
