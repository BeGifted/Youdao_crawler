"""
字符串和常用数据结构

version: 0.1
Author: gongyuandaye
"""

s1 = r'\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = 'hello ' * 3
print(s1) # hello hello hello 
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45

len(s1)
s1.find('')

a, b = 1, 2
print(f'{a} * {b} = {a * b}')
print('%d * %d = %d' % (a, b, a * b))

list1 = [5, 4, 3, 2, 1]
list2 = sorted(list1)
for i in range(len(list2)):
    print(list2[i])