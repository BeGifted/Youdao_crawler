"""
语言元素

version: 0.1
Author: gongyuandaye
"""

print(3 == 5)

a = 11
b = 4
print(a + b)
print(a - b)
print(a / b)
print(a // b) #保留小数点前整数
print(a ** b) #a^b
print(a * b)

print(type(a)) #输出元素类型

c = int(input('c = '))
d = int(input('d = '))
print('%d + %d = %d' % (c, d, c + d))

print(not b > a and c == d)