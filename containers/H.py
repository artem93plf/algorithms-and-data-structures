from collections import deque
import sys

input = sys.stdin.readline

left_deque = deque()
right_deque = deque()

n = int(input())

for _ in range(n):
    input_str = input().split()
    if input_str[0] == "+":
        right_deque.append(int(input_str[1]))
    elif input_str[0] == "*":
        left_deque.append(int(input_str[1]))
    elif input_str[0] == "-":
        print(left_deque.popleft())

    if len(left_deque) < len(right_deque):
        left_deque.append(right_deque.popleft())
    elif len(left_deque) > len(right_deque) + 1:
        right_deque.appendleft(left_deque.pop())