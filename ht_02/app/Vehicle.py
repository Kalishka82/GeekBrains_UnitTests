from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, company: str, model: str, release_year: int) -> None:
        self._company = company
        self._model = model
        self._release_year = release_year
        self._wheels_num = 0
        self._speed = 0

    @abstractmethod
    def drive(self) -> None:
        ...

    @abstractmethod
    def park(self) -> None:
        ...

    @property
    def company(self):
        return self._company

    @property
    def model(self):
        return self._model

    @property
    def release_year(self):
        return self._release_year

    @property
    def wheels_num(self):
        return self._wheels_num

    @property
    def speed(self):
        return self._speed
