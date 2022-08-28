from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    """
    Абстрактный класс со всеми необходимыми методами
    """

    @abstractmethod
    def add(self, name: str, amount: int) -> None:  # добавляем товар
        pass

    def remove(self, name: str, amount: int) -> None:  # удаляем товар
        pass

    def get_free_space(self) -> int:  # проверка свободного места
        pass

    def get_items(self):  # список товаров в местах хранения
        pass

    def get_unique_items_count(self):  # проверка количества уникальных товаров
        pass
