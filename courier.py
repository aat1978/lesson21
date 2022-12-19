from typing import Dict

from abstract_storage import AbstractStorage
from request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.__from = storages[self.__request.departure]
        self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.departure}")

        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}")

