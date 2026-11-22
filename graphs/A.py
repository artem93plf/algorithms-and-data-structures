n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

flag = True

for i in range(n):
    if arr[i][i] != 0:
        flag = False
        break

    for j in range(n):
        if arr[i][j] != arr[j][i]:
            flag = False
            break

print("YES" if flag else "NO")