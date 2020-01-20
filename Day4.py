"""
循环结构

version: 0.1
Author: gongyuandaye
"""

import random
import math
#from math import sqrt

sum = 0
for x in range(1, 100, 2): #1-99 奇数
    sum += x
print(sum)

#while True:

rand = random.randint(1, 100) #1-100随机数
num = int(math.sqrt(rand))
print(num)