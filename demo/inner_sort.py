# -*- coding: UTF-8 -*-
import time

from common import createData

"""
最坏时间复杂度
O(n^2)
最优时间复杂度
O(n)
平均时间复杂度
O(n^2)
空间复杂度
总共{O(n)}
需要辅助空间{ O(1)}
稳定的排序
"""

L = createData.random_int_list(1, 100, 10)


def innersort(arr):
    """简洁版本"""
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr


def innersort1(arr):
    """普通版本"""
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            temp = arr[j]
            if arr[j] < arr[j-1]:
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            else:
                break
    return arr


def innersort2(arr):
    """
    优化版插入排序
    使用二分查找函数确定待插入元素在有序区间的插入位置
    """
    length = len(arr)
    for i in range(1, length):  # 默认第一个位置的元素是已排序区间，因此下标从 1 开始
        wait_insert_data = arr[i]  # 等待插入元素
        move_index = i
        insert_index = binary_search(arr[0:i], wait_insert_data)  # 寻找插入位置
        while move_index > insert_index:  # 移动元素，直到待插入位置处
            arr[move_index] = arr[move_index - 1]
            move_index -= 1
        arr[insert_index] = wait_insert_data  # 插入操作
        # 另种写法
        # while move_index > inner_index:
        #         #     arr[move_index], arr[move_index-1] = arr[move_index-1], arr[move_index]
        #         #     move_index -= 1
    return arr


def binary_search(data_list,data):
    """
    二分法确定插入位置
    :param data_list: 有序列表
    :param data: 和待查找的数据data
    :return: 插入位置
    """
    length = len(data_list)
    low = 0
    high = length-1
    # 如果给定元素大于等于最后一个元素，则插入最后元素位置的后面
    # 如果小于第一个元素，则插入位置0
    if data >= data_list[length-1]: return length
    elif data < data_list[0]: return 0
    insert_index = 0
    while low < high-1:
        mid = (low + high)//2  # python中的除法结果默认为浮点数取整数部分时使用 //
        if data_list[mid] > data:
            high = mid
            insert_index = high
        else:
            low = mid
            insert_index = low+1  # 如果值相同或者值大于mid的值，那么插入位置位于其后面
    return insert_index


print(L)
stime = time.time()
print(innersort1(L))
# print(time.time() - stime)
