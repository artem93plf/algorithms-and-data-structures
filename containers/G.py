stack = []

n = int(input())
way1 = list(map(int, input().split()))

v = 1
for i in range(n):
    stack.append(way1[i])
    while stack and stack[-1] == v:
        stack.pop()
        v += 1

print('NO' if stack else 'YES')

