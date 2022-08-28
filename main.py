from exceptions import BaseError
from logistics.courier import Courier
from logistics.requests import Request
from logistics.shop import Shop
from logistics.store import Store

store = Store(items={
    'печенька': 25,
    'собачка': 25,
    'коробка': 25,
})

shop = Shop({
    'печенька': 2,
    'собачка': 2,
    'коробка': 2,
})

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    print('Приветствую\n')

    while True:

        # состояние склада
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        # запрос пользователя
        user_input = input(
            'Введите запрос вида "Доставить 3 печенька из склад в магазин"\n'
            'Введите "стоп" или "stop", если желаете закончить\n'
        )

        if user_input in ["стоп", "stop"]:
            break

        # формирование запроса на перемещение
        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)

        # перемещение товара
        try:
            courier.move()
        except BaseError as error:
            print(error.message)
            courier.cancel()


if __name__ == '__main__':
    main()
