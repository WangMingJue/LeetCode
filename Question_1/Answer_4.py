"""
1. 先对nums列表进行字典化，形成 [元素值]为键，[元素位置]为值的tmp_dict字典
2. 对nums进行循环，然后获取第i个元素的差值A
3. 如果差值A在tmp_dict字典的键中，且差值位置不等于当前位置的话，就是正确的值
注：执行用时大量减少的原因在于，字典的查找时间比列表的查找时间短非常多
"""
nums = [3, 2, 4, 5, 5]
target = 10

tmp_dict = {}
for index, value in enumerate(nums):
    tmp_dict[value] = index
for i in range(len(nums)):
    tmp = target - nums[i]
    if tmp in tmp_dict.keys() and tmp_dict[tmp] != i:
        print([i, tmp_dict[tmp]])
        break
"""
执行用时：44 ms, 在所有 Python3 提交中击败了43.19%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了5.18%的用户
"""
