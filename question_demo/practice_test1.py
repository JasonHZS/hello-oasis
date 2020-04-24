"""
翻转字符串“algorithm”
"""
s = 'zxcvbnma'
s_list = list(s)
i=0
j=len(s)-1
while i < j:
    s_list[i],s_list[j] = s_list[j],s_list[i]
    i += 1
    j -= 1
# print(''.join(s_list))


"""
给定两个字符串 s 和 t，编写一个函数来判断 t 是否是 s 的字母异位词。
字母异位词，也就是两个字符串中的相同字符的数量要对应相等。例如，s等于“anagram”，t等于“nagaram”，s和t就互为字母异位词。
因为它们都包含有三个字符a，一个字符g，一个字符m,一个字符 n，以及一个字符 r。而当 s 为 “rat”，t 为 “car”的时候，s 和 t 不互为字母异位词。

"""
s = "aacc"
t = "ccac"


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    for char in t:
        if char in d:
            d[char] -= 1
        else:
            return False

    for k in d:
        if d[k] != 0: return False

    return True


"""
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
"""
temperatures = [73, 74, 75, 71, 69, 72, 76, 71]


def dailyTemperatures(T):
    """
    自己写的
    :param T:
    :return:
    """
    temp = [0]
    ans = [0]*len(T)
    for i in range(1, len(T)):
        last_tindex = len(temp)
        if T[i] <= T[temp[last_tindex-1]]:
            temp.append(i)
        else:
            while T[i] > T[temp[last_tindex-1]]:
                top = temp.pop()
                ans[top] = i - top
                if len(temp) == 0: break
                else: last_tindex = len(temp)
            temp.append(i)
    return ans


def dailyTemperatures1(T):
    """
    官方的
    :param T:
    :return:
    """
    ans = [0] * len(T)
    stack = []  # indexes from hottest to coldest
    for i in range(len(T) - 1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans


print(dailyTemperatures(temperatures))