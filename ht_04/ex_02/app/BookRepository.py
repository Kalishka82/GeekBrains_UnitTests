from ht_04.ex_02.app import Book


class BookRepository:
    def __init__(self):
        self._books = []

    def find_all(self) -> list[Book]:
        return self._books

    def find_by_id(self, book_id: int):
        for book in self._books:
            if book.id == book_id:
                return book
