c = float(input())

left = 0
right = c
while right - left > 1e-6:
    mid = (left + right) / 2
    if mid ** 2 + mid ** 0.5 < c:
        left = mid
    else:
        right = mid
print((left + right) / 2)

