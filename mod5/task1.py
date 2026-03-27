class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        cur = self.end
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.pref
        print()


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push('AAA')
s.print()
print(s.pop())
s.print()