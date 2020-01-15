# -*- coding: UTF-8 -*-
import random


def random_int_list(start, stop, length):
    """
    造随机数组
    :param start: 数据最小值
    :param stop: 数据最大值
    :param length: 长度
    :return: 数据
    """
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list