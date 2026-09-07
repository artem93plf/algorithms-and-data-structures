str1 = input()
str2 = input()

counts = {}

if len(str1) != len(str2):
    print("NO")
else:
    for i in str1:
        counts[i] = counts.get(i, 0) + 1
    for i in str2:
        counts[i] = counts.get(i, 0) - 1
    for value in counts.values():
        if value != 0:
            print("NO")
            break
    else:
        print("YES")