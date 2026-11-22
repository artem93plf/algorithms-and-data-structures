n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

ki = 0
ks = 0
bomjara = 0 
ki_arr = []
ks_arr = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            bomjara += 1
    if bomjara == n:
        ks += 1
        ks_arr.append(i + 1)
    bomjara = 0

for i in range(n):
    for j in range(n):
        if arr[j][i] == 0:
            bomjara += 1
    if bomjara == n:
        ki += 1
        ki_arr.append(i + 1)
    bomjara = 0

print(ki)
for i in ki_arr:
    print(i)
print(ks)
for i in ks_arr:
    print(i)

    
