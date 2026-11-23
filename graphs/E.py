import sys 
sys.setrecursionlimit(200000)

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]

# доб инд-элемент соседей котрого мы пишем сюда
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

visited = [False] * (n + 1)
components = []

def dfs(v):
    visited[v] = True
    component.append(v)

    for i in a[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, n + 1):
    if not visited[i]:
        component = []
        dfs(i)
        components.append(component)

print(len(components))

for c in components:
    print(len(c))
    print(*c)