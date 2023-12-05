class Book:
    def __init__(self, book_id: int, title: str = None, author: str = None):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.book_id == other.book_id
                and self.title == other.title
                and self.author == other.author)

    def get_id(self):
        return self.book_id

    def set_id(self, book_id: int):
        self.book_id = book_id

    def get_title(self):
        return self.title

    def set_title(self, title: str):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author: str):
        self.author = author
