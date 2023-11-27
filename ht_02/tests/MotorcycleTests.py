import unittest

from ht_02.app.Motorcycle import Motorcycle
from ht_02.app.Vehicle import Vehicle


class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        self.motorcycle = Motorcycle('Suzuki', 'Hayabusa', 1999)

    def tearDown(self) -> None:
        self.motorcycle = None

    def test_instance_of(self):
        """ Проверим, что экземпляр объекта Motorcycle также
        является экземпляром транспортного средства Vehicle. """
        self.assertTrue(isinstance(self.motorcycle, Vehicle))

    def test_wheels(self):
        """ Проверим, что объект Motorcycle создается с 2-мя колесами. """
        self.assertEqual(self.motorcycle.wheels_num, 2)

    def test_drive(self):
        """ Проверим, что объект Motorcycle развивает скорость 75 в режиме тестового вождения. """
        self.assertEqual(self.motorcycle.speed, 0)
        self.motorcycle.drive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_park(self):
        """ Проверим, что в режиме парковки (сначала testDrive, потом park,
        те эмуляция движения транспорта) мотоцикл останавливается (speed = 0). """
        self.motorcycle.drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
