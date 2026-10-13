from collections import deque

first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

moves = 0
limit = 10**6

while first and second and moves < limit:
    x = first.popleft()
    y = second.popleft()

    if x == 0 and y == 9:
        first_wins = True
    elif x == 9 and y == 0:
        first_wins = False
    else:
        first_wins = x > y

    if first_wins:
        first.append(x)
        first.append(y)
    else:
        second.append(x)
        second.append(y)

    moves += 1

if not first:
    print("second", moves)
elif not second:
    print("first", moves)
else:
    print("botva")