from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)

    def add_member(self, name, member_id):
        new_member = Member(name, member_id)
        self.members.append(new_member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title and not book.checked_out:
                return book
        return None

    def check_out_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = self.find_book(book_title)
        if member and book:
            member.check_out_book(book)
            print(f"Book '{book_title}' checked out by {member.name}.")
        else:
            print("Book or member not found.")

    def return_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in member.books_checked_out if b.title == book_title), None)
        if member and book:
            member.return_book(book)
            print(f"Book '{book_title}' returned by {member.name}.")
        else:
            print("Book or member not found.")
