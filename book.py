class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        else:
            return False

    def return_book(self):
        self.checked_out = False
