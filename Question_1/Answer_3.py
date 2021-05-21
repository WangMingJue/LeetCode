"""
1. 使用map函数，依次使用Target减去每个元素，得到一个差值列表A
2. 循环差值列表A
3. 获取第i个原值的位置
4. 再获取nums[i+1]子列表中，差值A在子列表中的位置
"""
nums = [3, 2, 4, 5, 5]
target = 10

for i in map(lambda x: target - x, nums):
    try:
        start_index = nums.index(target - i)
        end_index = nums[start_index + 1:].index(i)
        print([start_index, end_index+start_index+1])
        break
    except:
        continue
"""
执行用时：852 ms, 在所有 Python3 提交中击败了5.00%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了24.23%的用户
"""
