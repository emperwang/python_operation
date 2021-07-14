#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def hello(greeting,*args):
    if(len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s' % (greeting, ','.join(args)))

hello('Hi') # => greeting='Hi' , args=()
hello('Hi','Sarah') #=> greeting='Hi', args=('Sarah')

# => greeting='hello' args=('Michael,Bob,Adam')
hello('Hello', 'Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')

#=> greting='hello', args=('Bart','Lisa')
hello('Hello', *names)