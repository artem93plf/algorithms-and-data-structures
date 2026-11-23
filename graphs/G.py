n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

if m == n - 1 and sum(visited) == n:
    print("YES")
else:
    print("NO")
