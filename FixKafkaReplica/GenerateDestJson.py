#/usr/bin/python3
# encoding=utf-8

import os
import json
import sys

BASE = os.getcwd()


def get_file_from_cmd():
    if len(sys.argv) > 2:
        print("filePath is: ", sys.argv[1])
    else:
        print("Usage : ", sys.argv[0], " filePath")


class analyseJson():

    def __init__(self, filePath, ids):
        self.filePath = filePath
        self.ids = ids

    def analyse(self):
        with open(self.filePath) as f:
            line = f.readline()
#            print(line)
            if "log_dirs" in line:
                self.__one(line)
            else:
                self.__many(line)

    def __one(self, content):
        print("one content: ", content)
        oneJson = json.loads(content)
        print("version: ", oneJson['version'])
        for itm in oneJson['partitions']:
            print(itm)

    def __many(self, content):
        print("many content: ", content)


def main():
    #fileName = "sourceOne.json"
    fileName = "sourceMany.json"
    filePath = (BASE+"/"+fileName).replace("\\", "/")
    print("base :", filePath)
    jsonAly = analyseJson(filePath, '1,2,3')
    jsonAly.analyse()


if __name__ == '__main__':
    main()