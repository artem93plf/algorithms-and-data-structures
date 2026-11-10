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

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0

        return 1 + self._size(node.left) + self._size(node.right)


tree = BinarySearchTree()

numbers = list(map(int, sys.stdin.read().split()))

for number in numbers:
    if number == 0:
        break
    tree.insert(number)

print(tree.size())