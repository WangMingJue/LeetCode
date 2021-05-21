"""
1. 先判断是否为负数，如果是的话，则直接返回False
2. 将x转为字符串类型，再转成列表类型
3. 对列表进行反转，再转化为数字类型
4. 如果反转后的数字大小跟x一样，那就返回True，反之为False
"""
x = 1534236469

if x < 0:
    print(False)
tmp = list(str(x))
tmp.reverse()
tmp = int("".join(tmp))
if tmp == x :
    print(True)
print(False)

"""
执行用时：68 ms, 在所有 Python3 提交中击败了82.36%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.32%的用户
"""
