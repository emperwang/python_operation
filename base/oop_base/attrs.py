#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

#有属性x吗
print('hasattr(obj, x) = ', hasattr(obj, 'x'))
print('hasattr(obj, y)', hasattr(obj, 'y'))
#设置一个属性
setattr(obj, 'y', 19)
print('hasattr(obj, y)=', hasattr(obj, 'y'))
#获取属性的值
print('getattr(obj,y)=', getattr(obj, 'y'))

print('obj.y = ', obj.y)

print('getattr(obj, z)=', getattr(obj, 'z', 404))
