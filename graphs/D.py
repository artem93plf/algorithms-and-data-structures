n, s = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n 

def dfs(v):
    visited[v] = True 

    for i in range(n):
        if a[v][i] == 1 and not visited[i]:
            dfs(i)

dfs(s - 1)

print(sum(visited))