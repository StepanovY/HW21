from typing import Dict

from exceptions import InvalidRequest, StoragesNameError
from logistics.abstract_storage import AbstractStorage


class Request:
    """
    Формирование запроса на перемещение товара
    """

    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):
        self.request = request

        requests = request.lower().split(' ')  # формируем из запроса список

        if len(requests) != 7:
            raise InvalidRequest

        self.amount = int(requests[1])  # количество
        self.product = requests[2]  # наименование товара
        self.departure = requests[4]  # откуда перемещаем
        self.delivery = requests[6]  # куда перемещаем

        if self.departure not in storages or self.delivery not in storages:  # проверка места куда/откуда перемещаем товар
            raise StoragesNameError
