class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return "ok"

    def isEmpty(self):
        return self.items == []
    
    def pop(self):
        if self.isEmpty():
            return "error"
        return self.items.pop()

    def back(self):
        if self.isEmpty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        return "ok"
    
    def exit(self):
        return "bye"

s = Stack()

while True:
    cmd = input().split()
    todo = cmd[0]
    if todo == "exit":
        print(s.exit())
        break
    elif todo == "push":
        print(s.push(int(cmd[1])))
    elif todo == "pop":
        print(s.pop())
    elif todo == "back":
        print(s.back())
    elif todo == "size":
        print(s.size())
    elif todo == "clear":
        print(s.clear())

