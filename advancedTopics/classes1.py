class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # toString() method
    def __str__(self):
        return f"Author {self.first_name} {self.last_name}"


class Book:
    # constructor
    def __init__(self, title: str, author: Author):
        self.title = title
        self.author = author

    # toString() method
    def __str__(self):
        return f"Book {self.title} by {self.author}"


book_1 = Book("1984", Author("George", "Orwell"))
print(book_1)
