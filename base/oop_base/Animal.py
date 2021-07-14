#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running....')

class Dog(Animal):
    def run(self):
        print('Dog is running..')

class Cat(Animal):
    def run(self):
        print('Cat is running')

def run_twicw(animal):
   animal.run()
   animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('d is Dog?', isinstance(d, Dog))
print('c is Cat?', isinstance(c, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twicw(c)