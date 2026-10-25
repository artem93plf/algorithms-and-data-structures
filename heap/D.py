import heapq

heap = []

while True:
    try:
        inp = input().split()
    except EOFError:
        break
    if inp[0] == "ADD":
        heapq.heappush(heap, -int(inp[1]))
    elif inp[0] == "CLEAR":
        heap.clear()
    elif inp[0] == "EXTRACT":
        if heap:
            print(-heapq.heappop(heap))
        else:
            print("CANNOT")

