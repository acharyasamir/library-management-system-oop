class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_checked_out = []

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}"

    def check_out_book(self, book):
        self.books_checked_out.append(book)
        book.check_out()

    def return_book(self, book):
        self.books_checked_out.remove(book)
        book.return_book()
