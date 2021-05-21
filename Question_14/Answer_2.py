"""
1. 先判断strs的个数，如果为0，则返回“”;如果为1，则返回那个元素
2. 对strs列表进行排序，方便相同字符串的顺序
3. 对strs列表进行for循环
4. 设置一个junge_str，这是想要匹配的前缀，初始为第一个元素本身，随着循环不断去除最后一个字符
5. 然后再用junge_str对整个sts进行循环，如果junge_str不匹配某个元素，就进行下一轮
"""


def get_is_same(self, junge_str, strs):
    for other in strs:
        try:
            if other.index(junge_str) != 0:
                return False
        except:
            return False
    return True


def longestCommonPrefix(self, strs):
    str_len = len(strs)
    if str_len == 0:
        return ""
    if str_len == 1:
        return strs[0]
    strs.sort()
    str_len = len(strs[0])
    junge_str = ""
    for i in range(str_len):
        junge_str = strs[0][:(-1) * i]
        if i == 0:
            junge_str = strs[0]
        if self.get_is_same(junge_str, strs):
            break
        else:
            junge_str = ""
            continue
    return junge_str


"""
执行用时：32 ms, 在所有 Python3 提交中击败了98%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了98.03%的用户
"""
