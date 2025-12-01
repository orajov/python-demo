"""Define your own class."""

class Book:
    category = "General"

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def short_description(self) -> str:
        return f"{self.title} by {self.author} ({self.pages} pages)"

    def __str__(self) -> str:
        return f"Book<{self.title}>"


if __name__ == "__main__":
    book = Book("Clean Code", "Robert C. Martin", 464)
    print(book)
    print("Category:", book.category)
    print(book.short_description())
