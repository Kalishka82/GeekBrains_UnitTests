import unittest
from unittest.mock import Mock

from ht_04.ex_02.app.Book import Book
from ht_04.ex_02.app.BookService import BookService


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_repository = Mock()
        self.book_service = BookService(book_repository=self.mock_repository)

    def test_find_all_books(self):
        expected_books = [
            Book(book_id=1, title='Преступление и наказание', author='Федор Достоевский'),
            Book(book_id=2, title='Гордость и предубеждение', author='Джейн Остен')]
        self.mock_repository.find_all.return_value = expected_books
        result = self.book_service.find_all_books()

        self.mock_repository.find_all.assert_called_once()
        self.assertEqual(result, expected_books)

    def test_find_book_by_id(self):
        expected_book = Book(book_id=111, title='Преступление и наказание', author='Федор Достоевский')
        self.mock_repository.find_by_id.return_value = expected_book

        result = self.book_service.find_book_by_id(book_id=111)

        self.mock_repository.find_by_id.assert_called_once_with(111)
        self.assertEqual(result, expected_book)


if __name__ == '__main__':
    unittest.main()
