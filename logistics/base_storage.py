from typing import Dict

from exceptions import NoFreeSpace, NotEnoughProduct
from logistics.abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):
    """
    Базовый класс, реализующий необходимые методы. Наследуется от абстрактного.
    """

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < amount:
            raise NoFreeSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self.__items or self.__items[name] < amount:
            raise NotEnoughProduct

        self.__items[name] -= amount

        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self) -> int:
        current_spase = 0
        for value in self.__items.values():
            current_spase += value
        return self.__capacity - current_spase  # свободное место

    def get_items(self) -> Dict[str, int]:
        return self.__items

    def get_unique_items_count(self) -> int:
        return len(self.__items)
