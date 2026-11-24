n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

order = list(map(int, input().split()))

pos = [0] * (n + 1)

for i in range(n):
    pos[order[i]] = i

for a, b in edges:
    if pos[a] > pos[b]:
        print("NO")
        break
else:
    print("YES")
