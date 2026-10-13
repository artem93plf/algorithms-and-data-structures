s = input().split()
stack = []
for c in s:
    if c.isnumeric():
        stack.append(int(c))
    else:
        b = stack.pop()
        a = stack.pop()
        if c == '+':
            res = a + b
        elif c == '-':
            res = a - b
        elif c == '*':
            res = a * b
        elif c == '/':
            res = a // b
        stack.append(res)
print(stack.pop())
            