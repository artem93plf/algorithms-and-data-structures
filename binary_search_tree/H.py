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

    def print_branches(self):
        self._print_branches(self.root)

    def _print_branches(self, node):
        if node is None:
            return

        self._print_branches(node.left)

        has_left = node.left is not None
        has_right = node.right is not None

        if has_left != has_right:
            print(node.data)

        self._print_branches(node.right)


tree = BinarySearchTree()

for value in sys.stdin.read().split():
    number = int(value)
    if number == 0:
        break
    tree.insert(number)

tree.print_branches()