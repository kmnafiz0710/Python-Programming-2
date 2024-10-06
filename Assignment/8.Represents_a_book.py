class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_description(self):
        return f"{self.title} by {self.author}, Pages:{self.pages}"

book1 = Book("1984", "George Orwell", 328)
print(book1.get_description())

book2 = Book("Statistics And Probability","M. Nurul Islam", 857)
print(book2.get_description())