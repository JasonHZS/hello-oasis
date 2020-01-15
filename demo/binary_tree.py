# -*- coding: UTF-8 -*-
from collections import Iterable
from common import createData
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    """定义节点类"""
    def __init__(self, value, left=None, right=None):
        self.value = value  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点


class BinaryTree(object):

    def __init__(self, seq=()):
        """定义树类"""
        assert isinstance(seq, Iterable)  # 确保输入的参数为可迭代对象
        self.root = None
        self.insert(*seq)

    def insert(self, *args):
        """插入节点，默认第一个为根节点"""
        if not args:
            return
        if not self.root:
            self.root = Node(args[0])
            # print(self.root.value)
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.value:
                    if not seed.right:
                        node = Node(i)
                        # print(node.value)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Node(i)
                        # print(node.value)
                        seed.left = node
                        break
                    else:
                        seed = seed.left

    # 尚未完成：只能遍历出左子树或右子树
    # def preorder(self, node=None):
    #     if node is None:
    #         node = self.root
    #         print(node.value)
    #     if node.right is not None:
    #         node = node.right
    #         print(node.value)
    #         self.preorder(node)
    #     if node.left is not None:
    #         node = node.left
    #         print(node.value)
    #         self.preorder(node)
    def preorder(self, root):
        """前序遍历"""
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def middleorder(self, root):
        """中序遍历"""
        if root is None:
            return
        self.middleorder(root.left)
        print(root.value)
        self.middleorder(root.right)

    def postorder(self, root):
        """后序遍历"""
        if root is None:
            return
        self.middleorder(root.left)
        self.middleorder(root.right)
        print(root.value)

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root is None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.value)
            if node.left is not None:
                myQueue.append(node.left)
            if node.right is not None:
                myQueue.append(node.right)

    def minNode(self):
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def maxNode(self):
        node = self.root
        while node.right:
            node = node.right
        return node


# 画二叉树
def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    if node.left:
        G.add_edge(node.value, node.left.value)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.value, node.right.value)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)


def draw(node):   # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()


ll = createData.random_int_list(1,100,10)
# print([64, 93, 54, 98, 48, 91, 69, 12, 13, 80])
tree = BinaryTree([64, 93, 54, 98, 48, 91, 69, 12, 13, 80])
# tree = BinaryTree(ll)
print(tree.level_queue(tree.root))
# draw(tree.root)

