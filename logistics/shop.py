from exceptions import TooManyDifferentProducts
from logistics.base_storage import BaseStorage


class Shop(BaseStorage):
    """Класс магазина"""
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        """
        Метод отличается от базового ограничением по количеству уникальных товаров
        """
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts
        super().add(name, amount)
