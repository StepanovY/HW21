class BaseError(Exception):
    message = 'Неожиданная ошибка'


class NoFreeSpace(BaseError):
    message = 'Нет свободного места'


class NotEnoughProduct(BaseError):
    message = 'Недостаточно товара на складе'


class TooManyDifferentProducts(BaseError):
    message = 'Слишком много разных товаров на складе'


class InvalidRequest(BaseError):
    message = 'Неправильный запрос. Попробуйте снова'


class StoragesNameError(BaseError):
    message = 'Выбран не известный пункт доставки или отправления'
