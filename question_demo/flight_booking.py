# -*- coding: UTF-8 -*-
# bookings = [[1,2,10],[2,3,20],[2,5,25]]
#
# result = [0]*5
# for arr in bookings:
#     for i in range(arr[0],arr[1]+1):
#         result[i-1] += arr[2]
#
# print(result)

######################################################


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
    print(split_str)

    for item in split_str:
        # if item[0] == '1' or '7' or '9':
            result = result + num_button[item[0]][(len(item)%5)-1]
            print(num_button[item[0]][(len(item)%5)-1])
        # if item[0] == '0':
        #     result = result + num_button[item[0]][(len(item)%2)-1]
        #     # print(num_button[item[:1]][(len(item)%2)-1])
        # else:
        #     result = result + num_button[item[0]][(len(item)%4)-1]
            # print(num_button[item[:1]][(len(item)%4)-1])

    return result


a = '22222 5555 22 666 00 88 888 77777 4444 666 44'

print(key_input(a))