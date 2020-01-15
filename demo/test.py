# -*- coding: UTF-8 -*-
from common import createData

lll = createData.random_int_list(1, 100, 10)


def innersort(arr):
    for i in range(1, len(arr)):
        move_index = i
        inner_v = arr[i]
        inner_index = binary_search(arr[0:i], inner_v)
        while move_index > inner_index:
            arr[move_index], arr[move_index-1] = arr[move_index-1], arr[move_index]
            move_index -= 1
    return arr


def binary_search(arr, data):
    high = len(arr)-1
    low = 0
    if data < arr[low]: return 0
    elif data >= arr[high]: return high+1
    inner_index = 0
    while low < high-1:
        mid = (low + high)//2
        if data > arr[mid]:
            low = mid
            inner_index = low+1
        else:
            high = mid
            inner_index = high
    return inner_index


print([33, 59, 90, 99, 21, 6, 31, 7, 18, 10])
print(innersort([33, 59, 90, 99, 21, 6, 31, 7, 18, 10]))
