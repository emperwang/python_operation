#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def print_scores(**kw):
    print('   Name score')
    print('---------------')

    for name,score in kw.items():
        print('%10s,%d'%(name,score))
    print()

print_scores(adam=99,lisa=88,bart=77)

data = {
    'Adam': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_into(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('-------------')
    print('  Name:%s' % name)
    print('   Gender:%s' % gender)
    print('   City:%s' % city)
    print('   Age:%s' % age)


print_into('Bob', gender='male', age=10)
print_into('Lisa', gender='male', city='shanghai', age=20)