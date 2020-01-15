# -*- coding: UTF-8 -*-
import time
from common import createData
"""
快速排序(quick sort)的采用了分治的策略。

分治策略指的是：
将原问题分解为若干个规模更小但结构与原问题相似的子问题。递归地解这些子问题，然后将这些子问题的解组合为原问题的解。
快排的基本思想是：
在序列中找一个划分值，通过一趟排序将未排序的序列排序成 独立的两个部分，其中左边部分序列都比划分值小，右边部分的序列比划分值大，此时划分值的位置已确认，然后再对这两个序列按照同样的方法进行排序，从而达到整个序列都有序的目的。

作者：一根薯条
链接：https://www.jianshu.com/p/2b2f1f79984e
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# 先来看一个 我更想称之为伪快排的快排代码：
def quick_sort1(array):
    """
    这段代码最关键的是pivot这个参数，这段代码里取序列的第一个元素，然后以这个元素为分组的基准，利用列表解析式使得它左边的值都比它小，
    右边的值都比它大。然后再分别对这些序列进行递归排序。

    这段代码虽然短小利于理解，但是其效率很低，主要体现在以下方面：

    分组基准的选取过于随便，不一定可以取到列表的中间值
    空间复杂度大，使用了两个列表解析式，而且每次选取进行比较时需要遍历整个序列。
    若序列长度过于小(比如只有几个元素)，快排效率就不如插入排序了。
    递归影响性能，最好进行优化。
    :param array:
    :return:
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        # print(pivot)
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        # print("left{}".format(less_than_pivot))
        more_than_pivot = [x for x in array[1:] if x > pivot]
        # print("right{}".format(more_than_pivot))
        result = quick_sort1(less_than_pivot) + [pivot] + quick_sort1(more_than_pivot)
        # print("排序中{}".format(result))
        return result


# 下面用Python写一个C风格的快排(这里可以体会到快排的精髓)：
def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)


def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L


def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left


L = [5, 9, 1, 11, 6, 7, 2, 4, 17, 3, 10, 44, 21, 56, 12, 32, 7, 1, 25, 66]
# stime = time.time()
print(quick_sort(L))
# print(time.time() - stime)
