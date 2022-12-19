from abc import ABC, abstractmethod
from typing import Dict


class AbstractStorage(ABC):
    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name: str, amount: int):
        if self.get_free_space() < amount:
            pass

        self._items[name] = self._items.get(name, 0) + amount

    @abstractmethod
    def remove(self, name: str, amount: int):
        if name not in self._items:
            pass

        if self._items[name] < amount:
            pass

    @abstractmethod
    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    @abstractmethod
    def get_items(self) -> Dict[str, int]:
        return self._items

    @abstractmethod
    def get_unique_items_count(self) -> int:
        return len(self._items)
