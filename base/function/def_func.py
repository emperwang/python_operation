#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math
'''
定义一个函数,如果参数类型不是int 或float  就报错
如果是整数就返回,负数就返回其绝对值
'''
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny

n = my_abs(-20)
print(n)

x,y = move(100,100,60,math.pi/6)

print(x,y)
