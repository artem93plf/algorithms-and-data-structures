import sys
from random import getrandbits


class Node:
    def __init__(self, key):
        self.key = key
        self.priority = getrandbits(64)
        self.left = None
        self.right = None


def rotate_right(node):
    child = node.left
    node.left = child.right
    child.right = node
    return child


def rotate_left(node):
    child = node.right
    node.right = child.left
    child.left = node
    return child


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
        if node.left.priority > node.priority:
            return rotate_right(node)
    elif key > node.key:
        node.right = insert(node.right, key)
        if node.right.priority > node.priority:
            return rotate_left(node)

    return node


def find_next(node, key):
    answer = -1

    while node is not None:
        if node.key < key:
            node = node.right
        else:
            answer = node.key
            node = node.left

    return answer


input = sys.stdin.readline
n = int(input())

root = None
last_answer = 0

for _ in range(n):
    command, value = input().split()
    x = int(value)

    if command == "+":
        root = insert(root, (x + last_answer) % 10**9)
        last_answer = 0
    else:
        last_answer = find_next(root, x)
        print(last_answer)