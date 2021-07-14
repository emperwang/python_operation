#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return  self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = student('bartSimpson', 59)
print('bart.get_name()=', bart.get_name())
bart.set_score(60)
print('bart.get_score()=', bart.get_score())
