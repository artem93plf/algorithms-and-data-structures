
n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

def binary_search_l(arr, x):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid
        else:
            right = mid
    return left

def binary_search_g(arr, x):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid
        else:
            left = mid
    return right

for x in arr_k:
    l = binary_search_l(arr_n, x)
    r = binary_search_g(arr_n, x)

    if l == -1:
        print(arr_n[r])
    elif r == len(arr_n):
        print(arr_n[l])

    elif x - arr_n[l] <= arr_n[r] - x:
        print(arr_n[l])

    else:
        print(arr_n[r])