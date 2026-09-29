A, X, B, Y, N = map(int, input().split())


def good(days):
    dima = (days - days // X) * A
    fedor = (days - days // Y) * B

    return dima + fedor >= N


left = 0
right = N

while right - left > 1:
    mid = (left + right) // 2

    if good(mid):
        right = mid
    else:
        left = mid

print(right)