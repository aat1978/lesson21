from exceptions import TypeManyProductsError
from storage import Storage
from typing import Dict


class Shop(Storage):
    def __init__(self, items: Dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int):
        if self.get_unique_items_count() >= 5:
            raise TypeManyProductsError

        super().add(name, amount)
