#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import functools


int2 = functools.partial(int, base=2)
hex2dec = functools.partial(int, base=16)


print('1000000 = ', int2('1000000'))
print('1010101=', int2('1010101'))

print(hex2dec('0x67'))
print(hex2dec('67'))
