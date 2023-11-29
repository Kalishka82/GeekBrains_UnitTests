import pytest


def even_odd_number(number: int) -> bool:
    return number % 2 == 0


class TestEvenOddNumber:

    def test_odd_number(self):
        """ Проверим четное число на четность"""
        assert even_odd_number(10) is True

    def test_even_number(self):
        """ Проверим нечетное число на нечетность"""
        assert even_odd_number(11) is False
