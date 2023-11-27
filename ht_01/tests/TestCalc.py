import pytest

from ht_01.app.Calculator import Calculator


class TestCalc():

    @classmethod
    def setUpClass(cls):
        ...

    @classmethod
    def tearDownClass(cls):
        ...

    def setup(self) -> None:
        self.calc = Calculator()

    def teardown(self) -> None:
        print('Calculation done')

    @pytest.mark.positive
    def test_add(self):
        """ Adding check. """
        assert self.calc.add(3, 2) == 5

    @pytest.mark.positive
    def test_subtract(self):
        """ Subracting check. """
        assert self.calc.subtract(3, 2) == 1

    @pytest.mark.positive
    def test_multiply(self):
        """ Multipling check. """
        assert self.calc.multiply(3, 2) == 6

    @pytest.mark.positive
    def test_divide(self):
        """ Dividing check. """
        assert self.calc.divide(4, 2) == 2

    @pytest.mark.negative
    def test_divide_by_zero(self):
        """ Dividing by zero check. """
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(1, 0)

    @pytest.mark.skip("off")
    def test_disabled(self):
        """ Skipped test. """
        pass

    @pytest.mark.parametrize('x', [1, 2, 5, 100],
                             ids=['y', '2y', '5y', '100y'])
    def test_multiply_by_2(self, x):
        """ Multipling y by x. """
        assert self.calc.multiply(x, 4) == x * 4

    @pytest.mark.positive
    def test_assert_array_equals(self):
        """ Array equality check. """
        expected = [1, 2, 3]
        actual = [1, 2, 3]
        assert expected == actual

    @pytest.mark.positive
    def test_discount(self):
        """ Discount check. """
        assert self.calc.calculate_discount(100, 20) == 80

    @pytest.mark.negative
    def test_negative_price(self):
        """ Negative price check. """
        with pytest.raises(ValueError):
            self.calc.calculate_discount(-100, 0)

    @pytest.mark.negative
    def test_bad_discount(self):
        """ Bad discount check. """
        with pytest.raises(ValueError):
            self.calc.calculate_discount(0, 220)
