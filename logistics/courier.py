from typing import Dict

from logistics.abstract_storage import AbstractStorage
from logistics.requests import Request


class Courier:
    """
    Реализация перемещения товара
    """

    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.delivery in storages:
            self.__to = storages[self.__request.delivery]

    def move(self):
        """
        Функция перемещения товара между 2 точками
        """
        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.departure}')

        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.delivery}')

    def cancel(self):
        """
        Метод возврата товара, если не хватило места
        """
        self.__from.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер вернул {self.__request.amount} {self.__request.product} в {self.__request.departure}')
