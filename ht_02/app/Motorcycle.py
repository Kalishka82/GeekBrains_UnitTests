from ht_02.app.Vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, company, model, release_year):
        super().__init__(company, model, release_year)
        self._wheels_num = 2
        self._speed = 0

    def drive(self) -> None:
        self._speed = 75

    def park(self) -> None:
        self._speed = 0

    def __str__(self):
        return f'Motorcycle {self._company} {self._model} {self._release_year} year'
