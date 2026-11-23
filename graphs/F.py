n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

color = [0] * n
cycle = False

def dfs(v):
    global cycle

    color[v] = 1

    for i in range(n):
        if a[v][i] == 1:
            if color[i] == 0:
                dfs(i)
            elif color[i] == 1:
                cycle = True

    color[v] = 2

for i in range(n):
    if color[i] == 0:
        dfs(i)

print(1 if cycle else 0)
