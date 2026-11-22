n, m = map(int, input().split())
arr = set()

for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    arr.add((a, b))

if len(arr) == n * (n - 1) // 2:
    print("YES")
else:
    print("NO")