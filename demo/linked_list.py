# -*- coding: UTF-8 -*-
class Node:

    def __init__(self, value =None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        # 测试基本功能，输出字符串
        return str(self.value)


# print(Node("text"))

# 手动创建链表
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
# print(node1)
node1.next = node2
node2.next = node3
# print(node1.next)


def backward(Node):
    """向后打印"""
    if Node == None: return
    backward(Node.next)
    print(Node)


# backward(node1)


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


L = create_linkList(3)
# print(L)


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        # 功能：输入头节点，返回链表长度
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter


# print(LinkedList(node1).__len__())


"""约瑟夫环"""
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
        print(cur.value)
        pre.next = cur.next
        cur.next = None
        cur = pre.next
    print(cur.value)