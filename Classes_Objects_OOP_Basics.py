
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

# Creating an instance of the Book class
my_book = Book("Python Basics", "John Doe", 450)
print("Is the book long?", my_book.is_long())
