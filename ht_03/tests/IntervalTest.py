import pytest

MIN_RANGE = 25
MAX_RANGE = 100


def number_in_interval(number: int):
    return MIN_RANGE < number < MAX_RANGE


class TestInterval:

    @pytest.mark.positive
    @pytest.mark.parametrize('number', [26, 80, 99],
                        ids=['крайнее нижнее число в интервале',
                             'число из середины интервала',
                             'крайнее верхнее число в интервале'])
    def test_number_in_interval(self, number):
        """ Проверим число из интервала"""
        assert number_in_interval(number) is True

    @pytest.mark.negative
    @pytest.mark.parametrize('number', [10, 25, 100, 110],
                        ids=['малое число вне интервала',
                             'малое граничное число вне интервала',
                             'большое граничное число вне интервала',
                             'большое число вне интервала'])
    def test_number_out_of_interval(self, number):
        """ Проверим число вне интервала"""
        assert number_in_interval(number) is False
