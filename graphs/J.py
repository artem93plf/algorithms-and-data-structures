n, m = map(int, input().split())

edges = []

for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

order = list(map(int, input().split()))

for a, b in edges:
    if order.index(a) > order.index(b):
        print("NO")
        break
else:
    print("YES")