n, a, b, w, h = map(int, input().split())


def good(x):
    width = a + 2 * x
    height = b + 2 * x

    cnt1 = (w // width) * (h // height)
    cnt2 = (w // height) * (h // width)

    return max(cnt1, cnt2) >= n


left = 0
right = max(w, h) + 1

while right - left > 1:
    mid = (left + right) // 2

    if good(mid):
        left = mid
    else:
        right = mid

print(left)