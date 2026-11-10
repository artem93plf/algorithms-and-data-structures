import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    node = root
    while True:
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
                break
            node = node.left
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
                break
            node = node.right
        else:
            break

    return root


def find_next(root, key):
    answer = -1
    node = root

    while node is not None:
        if node.key >= key:
            answer = node.key
            node = node.left
        else:
            node = node.right

    return answer


input = sys.stdin.readline
n = int(input())

root = None
last_answer = 0

for _ in range(n):
    command, value = input().split()
    x = int(value)

    if command == "+":
        key = (x + last_answer) % 10**9
        root = insert(root, key)
        last_answer = 0
    else:
        last_answer = find_next(root, x)
        print(last_answer)
