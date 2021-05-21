"""
使用两重循环：
1. 第一重循环，依次获取第i个元素，然后使用Target减去这个元素，得到差值A
2. 第二重循环，在第i个元素后的列表中，去查找是否存在差值A，如果存在，这就是我们要找的
"""
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    tmp = target - nums[i]
    for j in range(i + 1, len(nums)):
        if nums[j] == tmp:
            print([i, j])
            break
        else:
            continue
"""
执行用时：2296 ms, 在所有 Python3 提交中击败了5.07%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.09%的用户
"""
