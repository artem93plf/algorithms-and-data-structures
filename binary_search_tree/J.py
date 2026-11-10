import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, key):
        self.data = key
        self.count = 1
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
        else:
            node.count += 1

        return node

    def print_frequencies(self):
        self._print_frequencies(self.root)

    def _print_frequencies(self, node):
        if node is None:
            return

        self._print_frequencies(node.left)
        print(node.data, node.count)
        self._print_frequencies(node.right)


tree = BinarySearchTree()

for value in sys.stdin.read().split():
    number = int(value)
    if number == 0:
        break
    tree.insert(number)

tree.print_frequencies()