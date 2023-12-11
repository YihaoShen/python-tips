"""
    折半查找:只适用于有序的顺序表
"""


def binary_search(L, key):
    low = 0
    high = len(L)
    mid = 0

    while low <= high:
        # /是浮点数除法, 要想使用整除就要使用//或者%
        mid = (low + high) // 2
        if L[mid] == key:
            return mid
        elif L[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [1, 3, 5, 6, 8, 9, 21, 34]
index = binary_search(arr, 8)
print(index)  # 4
