from ht_02.app.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company, model, release_year):
        super().__init__(company, model, release_year)
        self._wheels_num = 4
        self._speed = 0

    def drive(self) -> None:
        self._speed = 60

    def park(self) -> None:
        self._speed = 0

    def __str__(self):
        return f'Car {self._company} {self._model} {self._release_year} year'
