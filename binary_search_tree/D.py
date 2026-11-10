import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)

        return node

    def second_max(self):
        node = self.root
        parent = None

        # Находим макс и запом его родителя
        while node.right is not None:
            parent = node
            node = node.right

        if node.left is not None:
            # Ищем макс в левом поддереве
            node = node.left
            while node.right is not None:
                node = node.right
            return node.data

        return parent.data


tree = BinarySearchTree()

numbers = list(map(int, sys.stdin.read().split()))

for number in numbers:
    if number == 0:
        break
    tree.insert(number)

print(tree.second_max())