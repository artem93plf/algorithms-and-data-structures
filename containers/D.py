class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        return 'ok'

    def pop(self):
        if self.is_empty():
            return 'error'
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return 'error'
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return 'ok'

    def exit(self):
        return 'bye'

q = Queue()

while True:
    i = input().split()
    cmd = i[0]
    if cmd == 'push':
        print(q.push(i[1]))
    elif cmd == 'pop':
        print(q.pop())
    elif cmd == 'front':
        print(q.front())
    elif cmd == 'size':
        print(q.size())
    elif cmd == 'clear':
        print(q.clear())
    elif cmd == 'exit':
        print(q.exit())
        break
    