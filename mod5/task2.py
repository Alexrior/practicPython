class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None    # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None

        val = self.start.data
        self.start = self.start.nref

        if self.start is not None:
            self.start.pref = None
        else:
            self.end = None

        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)

        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)

        if n <= 0 or self.start is None:
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            else:
                self.end = new_node
            self.start = new_node
            return

        cur = self.start
        index = 0

        while cur is not None and index < n:
            cur = cur.nref
            index += 1

        if cur is None:
            self.push(val)
            return

        prev_node = cur.pref
        new_node.pref = prev_node
        new_node.nref = cur
        prev_node.nref = new_node
        cur.pref = new_node

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        cur = self.start
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.nref
        print()


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.print()
q.insert(1, 99)
q.print()
print(q.pop())
q.print()