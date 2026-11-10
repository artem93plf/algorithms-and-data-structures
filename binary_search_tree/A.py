import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.data:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

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

    def _max_node(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            max_node = self._max_node(node.left)
            node.data, max_node.data = max_node.data, node.data
            node.left = self._delete(node.left, key)

        return node

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        if node is None:
            return

        self._print_tree(node.left, level + 1)
        print("." * level + str(node.data))
        self._print_tree(node.right, level + 1)


tree = BinarySearchTree()

for line in sys.stdin:
    command = line.split()

    if command[0] == "PRINTTREE":
        tree.print_tree()
    else:
        key = int(command[1])

        if command[0] == "ADD":
            if tree.search(key):
                print("ALREADY")
            else:
                tree.insert(key)
                print("DONE")

        elif command[0] == "DELETE":
            if tree.search(key):
                tree.delete(key)
                print("DONE")
            else:
                print("CANNOT")

        elif command[0] == "SEARCH":
            if tree.search(key):
                print("YES")
            else:
                print("NO")