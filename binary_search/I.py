def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    first = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= x:
            if arr[mid] == x:
                first = mid
            right = mid - 1
        else:
            left = mid + 1

    if first == -1:
        return 0

    left = 0
    right = len(arr) - 1
    last = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= x:
            if arr[mid] == x:
                last = mid
            left = mid + 1
        else:
            right = mid - 1

    return last - first + 1


n = int(input())
arr_n = list(map(int, input().split()))

m = int(input())
arr_m = list(map(int, input().split()))

arr_n.sort()

for x in arr_m:
    print(binary_search(arr_n, x))