from abstract_storage import AbstractStorage


class Shop(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int):
        if self.get_unique_items_count() >= 5:
            pass

        super().add(name, amount)
