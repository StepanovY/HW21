from logistics.base_storage import BaseStorage


class Store(BaseStorage):
    """
    Класс склада, полностью наследуется от базового
    """

    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)
