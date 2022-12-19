from storage import Storage
from typing import Dict


class Store(Storage):
    def __init__(self, items: Dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)
