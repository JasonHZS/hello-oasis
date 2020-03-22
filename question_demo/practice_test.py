# -*- coding: UTF-8 -*-
from common import createData

"""
航班预订问题
解法：差分序列性质/前缀和

这里有 n 个航班，它们分别从 1 到 n 进行编号。
我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。
请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。

示例：
输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000
"""
bookings_list = [[1,2,10],[2,3,20],[2,5,25]]


def flight_booking(bookings, n):
    """
    暴力解法
    :param bookings:
    :param n:
    :return:
    """
    result = [0] * n
    for arr in bookings:
        for i in range(arr[0], arr[1] + 1):
            result[i - 1] += arr[2]
    return result


def corpFlightBookings(bookings, n):
    """
    差分序列性质/前缀和
    :param bookings:
    :param n:
    :return:
    """
    res = [0] * (n + 1)
    for i, j, k in bookings:
        res[i - 1] += k
        res[j] -= k
    for i in range(1, len(res)):
        res[i] += res[i - 1]
    return res[:-1]


# print(corpFlightBookings(bookings_list, 5))

#######################################################################

"""
九宫格输入
[ 1,.?! ] [ 2ABC ] [ 3DEF  ]
[ 4GHI  ] [ 5JKL ] [ 6MNO  ]
[ 7PQRS ] [ 8TUV ] [ 9WXYZ ]
          [ 0空  ]
中括号[ ]仅为了表示键盘的分隔，不是输入字符。
每个中括号中，位于首位的数字字符即是键盘的按键，按一下即可输入该数字字符。
多次按同一个键，则输入的字符依次循环轮流，例如按两次3，则输入D；按5次7，则输入S；按6次2，则输入A。
按键0的输入组合是0和空格字符，即按两次0输入空格。

你需要对于给定的按键组合，给出该组合对应的文本。

输入样例:22 5555 22 666 00 88 888 7777 4444 666 44
输出样例:ALAN TURING
"""


def key_input(str):
    """
    九宫格输入
    :param str: 输入字符串
    :return: 对应字符串
    """
    num_button = {'1': ['1', ',', '.', '?', '!'],
                  '2': ['2', 'A', 'B', 'C'],
                  '3': ['3', 'D', 'E', 'F'],
                  '4': ['4', 'G', 'H', 'I'],
                  '5': ['5', 'J', 'K', 'L'],
                  '6': ['6', 'M', 'N', 'O'],
                  '7': ['7', 'P', 'Q', 'R', 'S'],
                  '8': ['8', 'T', 'U', 'V'],
                  '9': ['9', 'W', 'X', 'Y', 'Z'],
                  '0': ['0', ' ']}
    result = ''
    split_str = str.split()
    # print(split_str)

    for item in split_str:
        if item[0] in ('1','7','9'):
            result = result + num_button[item[0]][(len(item)%5) - 1]
        if item[0] == '0':
            result = result + num_button[item[0]][(len(item)%2)-1]
        else:
            result = result + num_button[item[0]][(len(item)%4)-1]

    return result


a = '22 5555 22 666 00 88 888 7777 4444 666 44'
# print(key_input(a))

####################################################################


"""约瑟夫环"""


class Node:

    def __init__(self, value =None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        # 测试基本功能，输出字符串
        return str(self.value)


def create_linkList(n):
    """
    自动创建链表,结点的值从1开始自增
    :param n: 链表结点数
    :return: 头结点
    """
    head = Node(1)
    pre = head
    for i in range(2, n+1):
        newnode = Node(i)
        pre.next = newnode
        pre = newnode
    pre.next = head
    return head


n = 7  # 总的个数
m = 4  # 数的数目
if m == 1: print(n)  # 如果是1的话，特殊处理，直接输出
else:
    head = create_linkList(n)
    pre = None
    cur = head
    while cur.next != cur: # 终止条件是节点的下一个节点指向本身
        for i in range(m-1):
            pre = cur
            cur = cur.next
        # print(cur.value)
        pre.next = cur.next
        cur.next = None
        cur = pre.next
    # print(cur.value)


def LastRemaining_Solution(n, m):
    """
    递推公式： f(N,M)=(f(N−1,M)+M)%N
    :param n: 总人数
    :param m: 数到m出局
    :return:
    """
    # 用列表来模拟环，新建列表range(n)，是n个小朋友的编号，这里从1开始
    if not n or not m:
        return -1
    lis = list(range(1,n+1))
    i = 0
    while len(lis) > 1:
        i = (m - 1 + i) % len(lis)  # 递推公式
        lis.pop(i)
    return lis[0]


# print(LastRemaining_Solution(8,4))


#####################################################################

"""士兵分子弹"""
num_l = createData.random_int_list(1, 10, 10)
# print(num_l)


def allocate():
    if min(num_l) == max(num_l):
        return num_l
    f = num_l[0] // 2 + num_l[0] % 2
    num_l[0] = f + num_l[-1] // 2 + num_l[-1] % 2
    for i, n in enumerate(num_l[1:]):
        c = n // 2 + n % 2
        num_l[i + 1] = f + c
        f = c
    print(num_l)
    allocate()


# allocate()

#################################################################

"""盛最多水的容器"""


def maxArea(l):
    i, j, res = 0, len(l) - 1, 0
    while i < j:
        if l[i] < l[j]:
            res = max(res, l[i] * (j - i))
            i += 1
        else:
            res = max(res, l[j] * (j - i))
            j -= 1
    return res


ll = [1,8,6,2,5,4,8,3,7]
print(maxArea(ll))