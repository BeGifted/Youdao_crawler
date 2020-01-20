"""
函数和模块的使用

version: 0.1
Author: gongyuandaye
"""

def fact(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))

if __name__ == "__main__": #是直接执行模块才运行
    pass