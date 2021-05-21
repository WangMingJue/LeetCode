"""
跟解答4的区别在于，从列表的第二个元素进行字典化
注：多次运行时间不同，多运行几次，就可以40ms了
"""
nums = [3, 2, 4, 5, 5]
target = 6

tmp_dict = {}
for index, value in enumerate(nums[1:]):
    tmp_dict[value] = index+1
for i in range(len(nums)):
    tmp = target - nums[i]
    if tmp in tmp_dict.keys() and tmp_dict[tmp] != i:
        print([i, tmp_dict[tmp]])
        break
"""
执行用时：40 ms, 在所有 Python3 提交中击败了67.58%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了5.18%的用户
"""
