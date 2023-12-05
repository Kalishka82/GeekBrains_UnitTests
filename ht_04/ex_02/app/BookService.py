from ht_04.ex_02.app import Book, BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def book_repository(self):
        return self._book_repository

    def find_all_books(self) -> list[Book]:
        return self._book_repository.find_all()

    def find_book_by_id(self, book_id: int) -> Book:
        return self._book_repository.find_by_id(book_id)
