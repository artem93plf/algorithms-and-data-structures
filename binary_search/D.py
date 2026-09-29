a, b, c, d = map(int, input().split())

left = -10 ** 9
right = 10 ** 9

def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d

for _ in range(100):
    mid = (left + right) / 2
    if a > 0:
        if f(mid) < 0:
            left = mid
        else:
            right = mid
    else:
        if f(mid) > 0:
            left = mid
        else:
            right = mid

print(left)
