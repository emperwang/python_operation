#!/usr/bin/python
# coding=UTF-8

import os

BASE = os.getcwd()


class person:

    def __init__(self, name):
        self._name = name
    # getter 方法
    @property
    def name(self):
        return self._name

    # name 的setter方法
    @name.setter
    def name(self, name):
        if not isinstance(name,str):
            print("must be string")
        self._name = name

    # name属性的删除方法, 添加此方法后使用 del方法就可以删除 name属性, 是name属性而不是 _name
    @name.deleter
    def name(self):
        del self._name
        print("delete attribute name")



def main():
    pp = person("孙权")
    print("getter " , pp.name)
    # setter
    pp.name = "刘备"
    print("getter: ", pp.name)

    # deleter 函数
    del pp.name
    print(pp.name)



if __name__ == '__main__':
    main()