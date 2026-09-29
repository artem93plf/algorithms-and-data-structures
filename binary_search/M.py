n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

def good(arr, k, r):
    cnt = 0
    for length in arr:
        cnt += length // r
    return cnt >= k

l = 0
r = max(arr) + 1

if sum(arr) < k:
    print(0)
    exit(0)

while r - l > 1:
    mid = (l + r) // 2
    if good(arr, k, mid):
        l = mid
    else:
        r = mid

print(l)