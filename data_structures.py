class Queue:
    def __init__(self, *args) -> None:
        self.items: list = [*args]

    def __add__(self, item: any) -> None:
        self.items.insert(0, item)

    def remove(self) -> any:
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items) + " Длинна: " + str(self.size())


