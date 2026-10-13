def good(s):
    valid = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    for c in s:
        if len(stack) > 0 and (stack[-1], c) in valid:
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0

s = input()
print("yes" if good(s) else "no")