import heapq

n = int(input())


heap = [] #хранит кортеж (когда родится след рыбка, инд акв)
fish = [] #хр кол рыбок в кажд акв 

for i in range(n):
    x = int(input())
    fish.append(x)

    t = max(1, 1000 - x)
    heapq.heappush(heap, (t, i)) #в мом t в i акв родится рыбка

current_time = 0
current_pos = 0

while True:
    t, pos = heapq.heappop(heap)

    if abs(pos - current_pos) > t - current_time:
        print(t)
        break

    current_time = t
    current_pos = pos

    fish[pos] += 1

    next_t = t + max(1, 1000 - fish[pos])

    heapq.heappush(heap, (next_t, pos))