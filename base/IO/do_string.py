#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO

# write to string io
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#Read from stringio
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())