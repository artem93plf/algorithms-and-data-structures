n, r, c = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()


def good(x):
    i = 0
    teams = 0
    skipped = 0

    while teams < r:
        if a[i + c - 1] - a[i] <= x:
            teams += 1
            i += c
        else:
            i += 1
            skipped += 1

            if skipped > n - r * c:
                return False

    return True


left = -1
right = a[-1] - a[0]

while right - left > 1:
    mid = (left + right) // 2

    if good(mid):
        right = mid
    else:
        left = mid

print(right)