dist = list(map(int, input().split()))
price = list(map(int, input().split()))
dist.sort()
price.sort(reverse=True)
i = 0
res = 0
while i < len(dist):
    res += dist[i] * price[i]
    i += 1
print(res)