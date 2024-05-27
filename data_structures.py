import collections


class Queue:
    """
    Класс Queue реализует очередь с использованием collections.deque, обеспечивая
    добавление и удаление элементов с асимптотической сложностью O(1).

    Атрибуты:
    ----------
    items : collections.deque
        Двусторонняя очередь для хранения элементов.

    Методы:
    -------
    add(self, item: any) -> 'Queue':
        Добавляет элемент в конец очереди. Возвращает сам объект Queue.

    remove(self) -> any:
        Удаляет и возвращает элемент из начала очереди.
        Вызывает исключение IndexError, если очередь пуста.

    size(self) -> int:
        Возвращает количество элементов в очереди.

    __str__(self) -> str:
        Возвращает строковое представление очереди и её размера.
    """

    def __init__(self, *args) -> None:
        self.items: collections.deque = collections.deque([*args])

    def add(self, item: any) -> None:
        self.items.append(item)
        return self

    def remove(self) -> any:
        if self.items:
            return self.items.popleft()
        raise IndexError("Remove from empty queue")

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"{list(self.items)} Длинна: {self.size()}"


class Stack:
    """
    Класс Stack реализует стек с использованием списка, обеспечивая добавление
    (push) и удаление (pop) элементов с асимптотической сложностью O(1).

    Атрибуты:
    ----------
    items : list
        Список для хранения элементов стека.

    Методы:
    -------
    push(self, item: any) -> 'Stack':
        Добавляет элемент на вершину стека. Возвращает сам объект Stack.

    remove(self) -> any:
        Удаляет и возвращает элемент с вершины стека.
        Вызывает исключение IndexError, если стек пуст.

    size(self) -> int:
        Возвращает количество элементов в стеке.
    """

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

    def __str__(self):
        return f"[{self.data}]->{self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        temp = Node(data=value)
        temp.set_next(self.head)
        self.head = temp

    def length(self) -> int:
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.get_next()
        return counter

    def search(self, value) -> bool:
        current = self.head
        while current:
            if current.get_data() == value:
                return True
            current = current.get_next()
        return False

    def remove(self, value) -> Node:
        if self.head.get_data() == value:
            current = self.head
            self.head = self.head.get_next()
            current.set_next(None)
            return current
        current = self.head
        previous: Node | None = None
        while current:
            if current.get_data() == value:
                previous.set_next(new_link=current.get_next())
                current.set_next(None)
                return current
            else:
                previous = current
                current = current.get_next()


# region Пример использования Queue
print('Очередь')
a = Queue(1, 2, 3)
print(a)  # [1, 2, 3] Длина: 3
a.add(4)
print(a)  # [1, 2, 3, 4] Длина: 4
print(a.remove())  # 1
print(a, end="\n\n")
# endregion

# region Пример использования Stack
print('Стек')
s = Stack(1, 2, 3)
print(s)  # [1, 2, 3] Длина: 3
s.push(4)
print(s)  # [1, 2, 3, 4] Длина: 4
print(s.remove())  # 4
print(s)  # [1, 2, 3] Длина: 3
s.push(5).push(6)
print(s)  # [1, 2, 3, 5, 6] Длина: 5
print(s.remove())  # 6
print(s.remove())  # 5
print(s, end='\n\n')  # [1, 2, 3] Длина: 3
# endregion

# region Пример использования LinkedList
# Добавление элементов
print('Связный список')
linked_list = LinkedList()
# Добавление элементов 10, 20, 30 в список:
linked_list.add(10)
linked_list.add(20)
linked_list.add(30)
print(linked_list.head)  # Ожидается: [30]->[20]->[10]->None

# Длина списка
print("Длина списка:")
print(linked_list.length())  # Ожидается: 3

# Поиск элементов
print("Поиск элемента 20:")
print(linked_list.search(20))  # Ожидается: True
print("Поиск элемента 40:")
print(linked_list.search(40))  # Ожидается: False

# Удаление элемента
print("Удаление элемента 20:")
linked_list.remove(20)
print(linked_list.head)  # Ожидается: [30]->[10]->None

# Длина списка после удаления
print("Длина списка после удаления элемента 20:")
print(linked_list.length())  # Ожидается: 2

# Удаление элемента, которого нет в списке
print("Попытка удалить элемент 40, которого нет в списке:")
linked_list.remove(40)
print(linked_list.head)  # Ожидается: [30]->[10]->None

# Удаление головы списка
print("Удаление головы списка (элемент 30):")
linked_list.remove(30)
print(linked_list.head)  # Ожидается: [10]->None

# Удаление последнего элемента
print("Удаление последнего элемента (элемент 10):")
linked_list.remove(10)
print(linked_list.head)  # Ожидается: None
# endregion
