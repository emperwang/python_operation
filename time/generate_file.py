#!/usr/bin/env python
# coding=UTF-8

import sys
import os
import time
from abc import ABCMeta, abstractmethod
import datetime


class generator(metaclass=ABCMeta):
    @abstractmethod
    def support(self, type):
        pass

    @abstractmethod
    def generate(self, stime, etime, sid, basepath, names):
        pass


class generator_manager():

    def __init__(self):
        self.generators = []

    def register(self, generator):
        self.generators.append(generator)

    def generate_file(self, type, stime, etime, sid, basepath, names):
        for generator in self.generators:
            if generator.support(type):
                generator.generate(stime, etime, sid, basepath, names)


class VimGenerator(generator):

    def __init__(self):
        self.namePattern = "%Y%m%d-%H%M%S"
        self.dirPattern = "%Y%m%d"
        self.type = "vim"

    def support(self, type):
        return self.type.lower() == type

    def generate(self, stime, etime, sid, basepath, names):
        while stime <= etime:
            dir = stime.strftime(self.dirPattern)
            fileDir = os.path.join(basepath, self.type, "pm", sid, dir)
            if not os.path.exists(fileDir):
                os.makedirs(fileDir)

            for name in names:
                # name = name.replace("time", (stime - datetime.timedelta(hours=8)).strftime(self.namePattern))
                name = (stime - datetime.timedelta(hours=8)).strftime(self.namePattern) + name
                file = os.path.join(fileDir, name)
                CreateFile(file, stime)
                print("file : ", file, ", filestamp: ", stime.strftime(self.namePattern))

            stime = stime + datetime.timedelta(minutes=15)


class PimGenerator(generator):

    def __init__(self):
        self.namePattern = "%Y%m%d-%H%M%S"
        self.dirPattern = "%Y%m%d"
        self.type = "pim"

    def support(self, type):
        return self.type.lower() == type

    def generate(self, stime, etime, sid, basepath, names):
        while stime <= etime:
            dir = stime.strftime(self.dirPattern)
            fileDir = os.path.join(basepath, self.type, "pm", sid, dir)
            if not os.path.exists(fileDir):
                os.makedirs(fileDir)

            name = (stime - datetime.timedelta(hours=8)).strftime(self.namePattern)
            file = os.path.join(fileDir, name)
            CreateFile(file, stime)
            fileTimeStamp = stime.strftime(self.namePattern)
            print("file : ", file, ", filestamp: ", fileTimeStamp)
            stime = stime + datetime.timedelta(minutes=15)


class EmsGenerator(generator):
    # 2021022408
    def __init__(self):
        self.dirPattern = "%Y%m%d%H"
        self.namePattern = "%Y%m%d%H%M%S"
        self.type = "ems"

    def support(self, type):
        return self.type.lower() == type

    # stime and endTime should be like 2020-02-24
    def generate(self, stime, etime, sid, basepath, names):
        while stime <= etime:
            dir = stime.strftime(self.dirPattern)
            fileDir = os.path.join(basepath, self.type, "pm", sid, dir)
            if not os.path.exists(fileDir):
                os.makedirs(fileDir)

            for name in names:
                name = name.replace("time", stime.strftime(self.namePattern))
                file = os.path.join(fileDir, name)
                fileTimeStamp = (stime + datetime.timedelta(minutes=26))
                CreateFile(file, fileTimeStamp)
                print("file : ", file, ", filestamp: ", fileTimeStamp.strftime(self.namePattern))

            stime = stime + datetime.timedelta(minutes=15)


def CreateFile(path, mkdifyTime):
    file = open(path, 'w')
    file.close()
    os.utime(path, (mkdifyTime.timestamp(), mkdifyTime.timestamp()))




if __name__ == '__main__':
    param = sys.argv
    type = param[1]
    sid = param[2]
    startTime = param[3]
    endTime = param[4]
    baseFile = param[5]
    names = param[6:]
    print("args: ", param)
    # type = "ems"
    # sid = "ems001"
    # startTime = "2021-02-2415:00:00"
    # endTime = "2021-02-2515:00:00"
    # names = ['GD-PM-CSCF-A001-V3.2.3-time-15.xml', 'GD-PM-CSCF-A001-V3.2.3-time-15.xml',
    #          'GD-PM-MME-A001-V3.2.0-time-15.xml',
    #          'GD-PM-MME-A001-V3.2.0-time-15.xml', 'GD-PM-PCF-A001-V1.1.0-time-15.xml']
    # baseFile = "collection"
    manager = generator_manager()
    manager.register(VimGenerator())
    manager.register(PimGenerator())
    manager.register(EmsGenerator())
    sTime = datetime.datetime.strptime(startTime, "%Y-%m-%d%H:%M:%S")
    eTime = datetime.datetime.strptime(endTime, "%Y-%m-%d%H:%M:%S")
    manager.generate_file(type, sTime, eTime, sid, baseFile, names)
