# Library Management System

library = {}

# Function to add books
def add_book():
    book_id = input("Enter book ID: ")
    book_name = input("Enter book name: ")
    library[book_id] = {"name": book_name, "issued": False}
    print("Book added successfully.")

# Function to issue books
def issue_book():
    book_id = input("Enter book ID to issue: ")
    if book_id in library and not library[book_id]["issued"]:
        library[book_id]["issued"] = True
        print("Book issued successfully.")
    else:
        print("Book not available or already issued.")

# Function to return books
def return_book():
    book_id = input("Enter book ID to return: ")
    if book_id in library and library[book_id]["issued"]:
        library[book_id]["issued"] = False
        print("Book returned successfully.")
    else:
        print("Invalid return request.")

# Function to search books
def search_book():
    book_name = input("Enter book name to search: ")
    found = False
    for book in library.values():
        if book["name"].lower() == book_name.lower():
            print("Book found:", book["name"])
            found = True
    if not found:
        print("Book not found.")

# Main program
while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        issue_book()
    elif choice == '3':
        return_book()
    elif choice == '4':
        search_book()
    elif choice == '5':
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice.")