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

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node is None:
            return

        self._print_tree(node.left)
        print(node.data, end="\n")
        self._print_tree(node.right)


tree = BinarySearchTree()

numbers = list(map(int, sys.stdin.read().split()))

for number in numbers:
    if number == 0:
        break
    tree.insert(number)

tree.print_tree()