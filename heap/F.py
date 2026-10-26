import heapq 
a = []
heap = []
n = int(input())
for i in range(n):
    inp = list(map(int, input().split()))
    a.append(inp)

a.sort()
for inp in a:
    if len(heap) == 0:
        heapq.heappush(heap, inp[0] + inp[1])
    elif heap[0] <= inp[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, inp[0] + inp[1])
    else:
        heapq.heappush(heap, inp[0] + inp[1])

print(len(heap))