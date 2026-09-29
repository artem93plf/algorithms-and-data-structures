m, n = map(int, input().split())

workers = []

for i in range(n):
    t, z, y = map(int, input().split())
    workers.append((t, z, y))


def count_balls(T, t, z, y):
    cycle = t * z + y

    cycles = T // cycle
    balls = cycles * z

    remaining = T % cycle
    balls += min(z, remaining // t)

    return balls


def good(T):
    total = 0

    for t, z, y in workers:
        total += count_balls(T, t, z, y)

    return total >= m


left = -1
right = 10**9

while right - left > 1:
    mid = (left + right) // 2

    if good(mid):
        right = mid
    else:
        left = mid


print(right)

remaining = m
answer = []

for t, z, y in workers:
    can = count_balls(right, t, z, y)

    take = min(can, remaining)
    answer.append(take)

    remaining -= take

print(*answer)