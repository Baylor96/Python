'''
def recursion(x):
    result = x
    for i in range(1,x):
        result = result * i
    return result
'''

def recursion(x):
    if x == 1:
        return 1
    else:
        return x * recursion(x-1)

number = int(input('请输入一个正整数：'))
result = recursion(number)
print("%d 的阶乘是：%d" % (number, result))