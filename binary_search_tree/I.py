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

    def is_balanced(self):
        return self._check_height(self.root) != -1

    def _check_height(self, node):
        if node is None:
            return 0

        left_height = self._check_height(node.left)
        if left_height == -1:
            return -1

        right_height = self._check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)


tree = BinarySearchTree()

for value in sys.stdin.read().split():
    number = int(value)
    if number == 0:
        break
    tree.insert(number)

if tree.is_balanced():
    print("YES")
else:
    print("NO")