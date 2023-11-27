import unittest

from ht_02.app.Car import Car
from ht_02.app.Vehicle import Vehicle


class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car('Ford', 'Fusion', 2008)

    def tearDown(self) -> None:
        self.car = None

    def test_instance_of(self):
        """ Проверим, что экземпляр объекта Car также
        является экземпляром транспортного средства Vehicle. """
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_wheels(self):
        """ Проверим, что объект Car создается с 4-мя колесами. """
        self.assertEqual(self.car.wheels_num, 4)

    def test_drive(self):
        """ Проверим, что объект Car развивает скорость 60 в режиме тестового вождения. """
        self.assertEqual(self.car.speed, 0)
        self.car.drive()
        self.assertEqual(self.car.speed, 60)

    def test_park(self):
        """ Проверим, что в режиме парковки (сначала testDrive, потом park,
        те эмуляция движения транспорта) машина останавливается (speed = 0). """
        self.car.drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
