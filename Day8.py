"""
面向对象编程基础

version: 0.1
Author: gongyuandaye
"""

class stu:
    def __init__(self, name):
        self.name = name

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}!')
    
def main():
    stu1 = stu('gongyuandaye')
    stu1.study('py')

if __name__ == "__main__":
    main()