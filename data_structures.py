class Queue:
    def __init__(self, *args) -> None:
        self.items: list = [*args]

    def add(self, item: any) -> None:
        self.items.append(item)
        return self

    def remove(self) -> any:
        if self.items:
            return self.items.pop(0)
        raise IndexError("Remove from empty queue")

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"{self.items} Длинна: {self.size()}"


class Stack:
    def __init__(self, *args) -> None:
        self.items: list = [*args]

    def push(self, item: any) -> None:
        self.items.append(item)
        return self

    def remove(self) -> any:
        if self.items:
            return self.items.pop()
        raise IndexError("Remove from empty queue")

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"{self.items} Длинна: {self.size()}"


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def get_data(self):
        return self.data


    def get_next(self):
        return self.next


    def set_next(self, new_link):
        self.next = new_link
        return self
    
# class LinkedLisk:
#     def __init__()


#region Пример использования Queue
a = Queue(1, 2, 3)
print(a)  # [1, 2, 3] Длина: 3
a.add(4)
print(a)  # [1, 2, 3, 4] Длина: 4
print(a.remove())  # 1
print(a, end="\n\n")
#endregion

#region Пример использования Stack
s = Stack(1, 2, 3)
print(s)           # [1, 2, 3] Длина: 3
s.push(4)
print(s)           # [1, 2, 3, 4] Длина: 4
print(s.remove())  # 4
print(s)           # [1, 2, 3] Длина: 3
s.push(5).push(6)
print(s)           # [1, 2, 3, 5, 6] Длина: 5
print(s.remove())  # 6
print(s.remove())  # 5
print(s)           # [1, 2, 3] Длина: 3
#endregion

