#!/usr/bin/python3
# coding=utf-8
import os
import sys

# get current path
base = os.getcwd()


class properties:

    def __init__(self, filePath):
        self.filePath = base + "\\" + filePath
        self.properties = {}

    def parse(self):
        try:
            fopen = open(self.filePath, 'r')
            for line in fopen:
                line = line.strip()
                if line.startswith("#") or len(line) <= 0:
                    continue
                print("line =", line)
                vals = line.split("=")
                self.properties[vals[0]] = vals[1]
        except Exception as e:
            raise e
        finally:
            fopen.close()

    def getkey(self, key):
        if key in self.properties:
            return self.properties[key]
        else:
            return ""

    def travelProperties(self):
        for itm in self.properties.items():
            print(itm)


def main():
    # get argv 从命令行获取具体要分析的文件
    '''
    if len(sys.argv) < 2:
        print(sys.argv[0], " path/fileName")
        sys.exit(1)
    '''
    pro = properties("file.properties")
    pro.parse()
    pro.travelProperties()


if __name__ == '__main__':
    main()