"""
分支结构

version: 0.1
Author: gongyuandaye
"""

username = input()
password = input()
if username == 'gongyuandaye' and password == '123456':
    print('pass!')
elif username == 'gongyuandaye' or password == '123456':
    print('half-pass!')
else:
    print('fail!')