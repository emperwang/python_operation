# coding=UTF-8

import py_compile
from distutils.core import setup
from setuptools import find_packages
import os

os.system(r'pip3 install --no-index --find-links=./packages -r requirements.txt')
# 把文件编译为二进制
if os.access('Main.py', os.X_OK):
      py_compile.compile(file='Main.py', cfile='main.pyc', optimize=-1)


setup(name='demo',
      version='1.0',
      packages = find_packages(),
      description = 'Demo for test',
      author='kai.wang',
      author_email='None',
      url='None'
      )
