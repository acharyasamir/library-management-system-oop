from library import Library

def display_menu():
    print("\nWelcome to the Library Management System!")
    print("Please choose an option:")
    print("1. Add a new book")
    print("2. Add a new member")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. List all books")
    print("6. List all members")
    print("7. Search for a book")
    print("8. Exit")

def main():
    my_library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            isbn = input("Enter the book's ISBN: ")
            my_library.add_book(title, author, isbn)
            print(f"Book '{title}' added successfully.")

        elif choice == "2":
            name = input("Enter the member's name: ")
            member_id = input("Enter the member's ID: ")
            my_library.add_member(name, member_id)
            print(f"Member '{name}' added successfully.")

        elif choice == "3":
            member_id = input("Enter the member's ID: ")
            book_title = input("Enter the book title: ")
            my_library.check_out_book(member_id, book_title)

        elif choice == "4":
            member_id = input("Enter the member's ID: ")
            book_title = input("Enter the book title: ")
            my_library.return_book(member_id, book_title)

        elif choice == "5":
            print("List of all books:")
            for book in my_library.books:
                status = "Checked out" if book.checked_out else "Available"
                print(f"{book.title} by {book.author} - {status}")

        elif choice == "6":
            print("List of all members:")
            for member in my_library.members:
                print(f"{member.name} (ID: {member.member_id})")

        elif choice == "7":
            title = input("Enter the book title to search for: ")
            book = my_library.find_book(title)
            if book:
                status = "Checked out" if book.checked_out else "Available"
                print(f"Book found: {book.title} by {book.author} - {status}")
            else:
                print("Book not found.")

        elif choice == "8":
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
