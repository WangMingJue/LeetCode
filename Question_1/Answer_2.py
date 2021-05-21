"""
1. 循环，依次获取第i个元素，然后使用Target减去这个元素，得到差值A
2. 对nums列表进行切片，获取nums[i+1]列表，也就是第i个元素后的子列表
3. 使用in运算符，查看差值A是否在子列表中，如果不在就直接下一次循环
4. 如果在子列表中，直接返回
"""
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    tmp = target - nums[i]
    if tmp not in nums[i + 1:]:
        continue
    print([i, nums[i + 1:].index(tmp) + i + 1])

"""
执行用时：484 ms, 在所有 Python3 提交中击败了5.00%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了85.64%的用户
"""
