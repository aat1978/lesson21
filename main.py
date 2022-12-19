from Shop import Shop
from courier import Courier
from exceptions import BaseError
from request import Request
from store import Store

shop = Shop(items={'печенька': 3, 'ноутбук': 2},)
store = Store(items={'печенька': 10, 'ноутбук': 20},)
storages = {'магазин': shop, 'склад': store}


def main():
    while True:
        for storage_name in storages:
            print(f"В {storage_name} хранится: {storages[storage_name].get_items()}")

        user_input = input(
            'Введите строку в формате "Доставить 3 печеньки из склада в магазин".\n'
            'Введите "stop" или "start", чтобы продолжить: ',
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request_str=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except BaseError as error:
            print(error.message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

