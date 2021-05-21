"""
1. 先设置一个字典来存放，罗马数字对应的十进制数字
2. 把字符串s中的每个字母都转换为相应的数字，形成一个数字列表result_list
3. 对这个result_list进行循环
4. 先检查当前第i个元素是否小于第i+1个元素，如果小于，就让第i+1个元素减去第i个元素，存放到result中，且index（指针）要加2
5. 如果不小于，则直接把第i个元素加到result里，index加1
"""
s = "MCMXCIV"

roma_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result_list = list(map(lambda x: roma_dict[x], s))
result_list_length = len(result_list)
result = 0
index = 0
while index < result_list_length:
    if index + 1 < result_list_length and result_list[index] < result_list[index + 1]:
        result += (result_list[index + 1] - result_list[index])
        index += 2
    else:
        result += result_list[index]
        index += 1
print(result)

"""
执行用时：44 ms, 在所有 Python3 提交中击败了97.84%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了95.35%的用户
"""
"""
roma_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        result_list = list(map(lambda x: roma_dict[x], s))
        result_list_length = len(result_list)
        result = 0
        index = 0
        while index < result_list_length:
            if index + 1 < result_list_length and result_list[index] < result_list[index + 1]:
                result += (result_list[index + 1] - result_list[index])
                index += 2
            else:
                result += result_list[index]
                index += 1
        return result
"""