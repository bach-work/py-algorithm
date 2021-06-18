# Закодируйте любую строку по алгоритму Хаффмана.
import heapq
from collections import Counter


class Node:
    """Узел дерева"""

    def __init__(self, left, right):
        self.right = right
        self.left = left

    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf:
    """Лист дерева"""

    def __init__(self, char):
        self.char = char

    def __str__(self):
        return 'Лист. Значение: {}'.format(self.char)

    def walk(self, code, path):
        code[self.char] = path or "0"


def hauffman(s):
    """Кодирует в Хауффмана"""
    node_lst = []
    for c, count in Counter(s).items():
        node_lst.append((count, len(node_lst), Leaf(c)))

    heapq.heapify(node_lst)
    count = len(node_lst)
    while len(node_lst) > 1:
        freq1, _count1, left = heapq.heappop(node_lst)
        freq2, _count2, right = heapq.heappop(node_lst)
        heapq.heappush(node_lst, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if len(node_lst) == 1:  # Если все прошло ОК
        root = node_lst[0][2]
        root.walk(code, "")
    return code


s = 'beep boop beer!'
print("Входная строка: {}".format(s))
code = hauffman(s)

for ch in sorted(code):
    print("{}: {}".format(ch, code[ch]))

print("Результат: {}".format(" ".join(code[ch] for ch in s)))

hauffman(s)
