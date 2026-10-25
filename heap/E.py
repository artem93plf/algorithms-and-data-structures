import heapq

n = int(input())
ls = list(map(int, input().split()))

heapq.heapify(ls)

total = 0

while n > 1:
    a = heapq.heappop(ls)
    b = heapq.heappop(ls)
    sum = a + b
    total += sum
    heapq.heappush(ls, sum)
    n -= 1

print(f'{(total * 0.05):.2f}')