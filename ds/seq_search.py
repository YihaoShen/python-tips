"""
    顺序查找(线性查找)
"""


def seq_search(L, key):
    i = 0
    for i in range(0, len(L), 1):
        if L[i] != key:
            pass
    if i > len(L):
        return -1
    return i


arr = [1,3,4,5,6,2,7]
pos = 5
print(seq_search(arr, pos))
