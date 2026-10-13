class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) < 1

    def push_front(self, item):
        self.items.insert(0, item)
        return 'ok'

    def push_back(self, item):
        self.items.append(item)
        return 'ok'

    def pop_front(self):
        if self.is_empty():
            return 'error'
        return self.items.pop(0)

    def pop_back(self):
        if self.is_empty():
            return 'error'
        return self.items.pop()

    def front(self):
        if self.is_empty():
            return 'error'
        return self.items[0]

    def back(self):
        if self.is_empty():
            return 'error'
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        return 'ok'

    def exit(self):
        return 'bye'

d = Deque()

while True:
    i = input().split()
    cmd = i[0]
    if cmd == 'push_front':
        print(d.push_front(i[1]))
    elif cmd == 'push_back':
        print(d.push_back(i[1]))
    elif cmd == 'pop_front':
        print(d.pop_front())
    elif cmd == 'pop_back':
        print(d.pop_back())
    elif cmd == 'front':
        print(d.front())
    elif cmd == 'back':
        print(d.back())
    elif cmd == 'size':
        print(d.size())
    elif cmd == 'clear':
        print(d.clear())
    elif cmd == 'exit':
        print(d.exit())
        break
