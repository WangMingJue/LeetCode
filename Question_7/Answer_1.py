"""
1. 先使用sign来存储x的正负符号，如果为负，则进行绝对值处理
2. 将x转化为字符串类型，再转化成列表类型
3. 然后反转列表，再转化成字符串类型，再转化成数字类型
4. 最后乘以正负符号
5. 判断反转后的数字是不是在[−2的31次方,  2的31次方 − 1]中，不在返回0，在的话返回x
"""
x = 1534236469

sign = 1
if x < 0:
    sign = -1
    x = abs(x)
tmp = list(str(x))
tmp.reverse()
tmp = int("".join(tmp))
tmp = tmp * sign
if tmp < -2 ** 31 or tmp > 2 ** 31 - 1:
    print(0)
print(tmp)

"""
执行用时：40 ms, 在所有 Python3 提交中击败了77.68%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了41.74%的用户
"""
