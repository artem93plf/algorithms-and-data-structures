import sys

data = sys.stdin.read().split()

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] + data[j] < data[j] + data[i]:
            data[i], data[j] = data[j], data[i]
print("".join(data))
        