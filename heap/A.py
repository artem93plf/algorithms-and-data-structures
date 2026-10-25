class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shift_up(self, i):
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shift_up(self.size)

    def shift_down(self, i):
        while i * 2 <= self.size:
            j = self.ind_max_child(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def ind_max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def delete_max(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shift_down(1)
        return removed


n = int(input())
h = MaxHeap()
for i in range(n):
    x = list(map(int, input().split()))
    if x[0] == 0:
        h.insert(x[1])
    else:
        print(h.delete_max())
