from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
s, t = map(int, input().split())

q = deque([[s]])
visited = [False] * (n + 1)
visited[s] = True

while q:
    path = q.popleft()
    v = path[-1]

    if v == t:
        print(len(path) - 1)
        if len(path) > 1:
            print(*path)
        break

    for i in range(1, n + 1):
        if a[v - 1][i - 1] == 1 and not visited[i]:
            visited[i] = True
            q.append(path + [i])
else:
    print(-1)
