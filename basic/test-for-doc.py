#!/usr/bin/python3
# coding=utf-8

class myException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

x=10
if x > 5:
    try:
        raise myException(2*1000)
    except myException as e:
        print("My Exception, value", e.value)