"""
1. 先判断strs的个数，如果为0，则返回“”;如果为1，则返回那个元素；如果""在列表中，也返回“”
2. 设置目前匹配的前缀长度prefix_length，默认为1
3. 以第一个元素为基准进行while循环，条件为prefix_length的长度不超过第一个元素的长度
4. 再进行strs的for循环，如果当前的前缀对于所有元素都匹配，就prefix_length加1，再进行匹配
5. 如果在对某个元素匹配的过程中，是False的话，就直接返回上一次匹配通过的前缀
"""
strs = ["abca", "aba", "aaab"]
def longestCommonPrefix(strs):
    strs_length = len(strs)
    if strs_length == 0 or "" in strs:
        return ""
    if strs_length == 1:
        return strs[0]

    prefix_length = 1
    result = strs[0][:prefix_length]
    while prefix_length <= len(strs[0]):
        for i in strs[1:]:
            if result in i and result == i[:prefix_length]:
                pass
            else:
                return result[:prefix_length - 1]
        prefix_length += 1
        result = strs[0][:prefix_length]
    return result


print(longestCommonPrefix(strs))

"""
执行用时：36 ms, 在所有 Python3 提交中击败了90.73%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了18.00%的用户
"""
