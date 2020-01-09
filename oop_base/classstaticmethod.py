#!/usr/bin/python
# coding=UTF-8

import os
BASE = os.getcwd()

class student:
    address = "bj"      # 此属性属于  类属性
    def __init__(self, name):
        self.name = name  # 此属性属于 实例属性

    def printinfo(self):
        print("info:", self.name)

    # 静态方法不能访问类的属性,相当于是一个独立的方法,只是放在类的作用域
    @staticmethod
    def staticprint():
        print("this is a independent function")
        # print(self.name)    # error, 不能访问类属性
    # 类方法,可以方法类的属性,不能访问实例属性
    @classmethod
    def classmethodfunc(self):
        print("this is class method, can visit class's property")
        print("class property:", self.address)  # 访问类属性
        # print("name:", self.name)       # 访问实例属性  error

    # 属性方法, 把方法变为属性,调用时不需要 (), 不能使用 del 删除属性
    @property
    def eat(self):
        print("eat :")

    @eat.setter   # 给属性赋值
    def eat(self, food):
        print("eating:", food)

def main():
    student.staticprint()
    stu = student("曹操")
    stu.classmethodfunc()
    # 调用eat方法
    stu.eat
    # 调用 @eat.setter 修饰的方法
    stu.eat = "NFC"


if __name__ == '__main__':
    main()