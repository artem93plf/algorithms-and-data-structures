from collections import deque

n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

moves = [
    (2, 1), (2, -1),
    (-2, 1), (-2, -1),
    (1, 2), (1, -2),
    (-1, 2), (-1, -2)
]

visited = [[False] * (n + 1) for _ in range(n + 1)]
visited[x1][y1] = True

q = deque([[(x1, y1)]])

while q:
    path = q.popleft()
    x, y = path[-1]

    if x == x2 and y == y2:
        print(len(path) - 1)
        for a, b in path:
            print(a, b)
        break

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 1 <= nx <= n and 1 <= ny <= n:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append(path + [(nx, ny)])
