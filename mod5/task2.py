#Создать класс. Очередь на структуре данных двусвязный список. 
class Node:
    """
    Узел двусвязного списка: хранит данные и две ссылки
    """
    def __init__(self, data):
        self.data = data  # Значение узла
        self.nref = None  # Ссылка на СЛЕДУЮЩИЙ узел (next reference)
        self.pref = None  # Ссылка на ПРЕДЫДУЩИЙ узел (previous reference)


class Queue:
    """
    Класс Очереди: элементы входят в 'end' и выходят из 'start'
    """

    def __init__(self):
        self.start = None  # Указатель на начало очереди (откуда берем)
        self.end = None    # Указатель на конец очереди (куда добавляем)

    def pop(self):
        """
        Извлечение элемента из начала очереди (первый зашедший)
        """
        if self.start is None: # Если очередь пуста
            return None

        val = self.start.data      # Запоминаем данные первого узла
        self.start = self.start.nref # Сдвигаем начало на следующий узел

        if self.start is not None:
            self.start.pref = None # У нового первого узла теперь нет предыдущего
        else:
            self.end = None        # Если узлов больше нет, обнуляем и конец

        return val

    def push(self, val):
        """
        Добавление элемента в конец очереди
        """
        new_node = Node(val)

        if self.start is None:     # Если очередь была пуста
            self.start = new_node  # Новый узел становится и началом,
            self.end = new_node    # и концом одновременно
        else:
            new_node.pref = self.end # Старый конец становится предыдущим для нового
            self.end.nref = new_node # У старого конца прописываем ссылку на новый
            self.end = new_node      # Теперь новый узел официально стал концом

    def insert(self, n, val):
        """
        Вставка элемента на конкретную позицию n
        """
        new_node = Node(val)

        # Если вставляем в самое начало или очередь пуста
        if n <= 0 or self.start is None:
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            else:
                self.end = new_node
            self.start = new_node
            return

        # Ищем узел, перед которым нужно вставиться
        cur = self.start
        index = 0
        while cur is not None and index < n:
            cur = cur.nref
            index += 1

        # Если индекс за пределами списка — просто добавляем в конец
        if cur is None:
            self.push(val)
            return

        # Вставляем узел «между» найденным cur и его соседом слева
        prev_node = cur.pref
        new_node.pref = prev_node
        new_node.nref = cur
        prev_node.nref = new_node
        cur.pref = new_node

    def print(self):
        """
        Вывод всех элементов от начала до конца
        """
        cur = self.start
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.nref
        print()


# Проверка работы
q = Queue()
q.push(1)      # Очередь: 1
q.push(2)      # Очередь: 1 2
q.push(3)      # Очередь: 1 2 3
q.print()      # Вывод: 1 2 3

q.insert(1, 99) # Вставляем 99 на позицию 1 (после первого элемента)
q.print()      # Вывод: 1 99 2 3

print(q.pop()) # Удаляем и выводим самый первый (1)
q.print()      # Вывод: 99 2 3
