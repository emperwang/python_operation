#/usr/bin/python3
# encoding=utf-8

import os
import json
import sys
import random

BASE = os.getcwd()


def get_file_from_cmd():
    if len(sys.argv) > 2:
        print("filePath is: ", sys.argv[1])
    else:
        print("Usage : ", sys.argv[0], " filePath , ids(like: 0,1,2)")


class analyseJson():

    """
     filePath: 内容是建议分配的json字符串文件全路径
     ids: kafka 所有有效的broker id
     factor: 副本因子，不可大于broker的数量
    """
    def __init__(self, filePath, ids, factor):
        self.filePath = filePath
        self.ids = ids.split(",")
        self.factor = factor
        if self.factor > len(self.ids):
            print("factor cann't bigger than the num of ids")
            sys.exit(1)
        else:
            self.index = len(self.ids) - factor

    # 把字符串都转换为整数
    def __get_int_ids(self):
        self.listids = []
        for i in self.ids:
            self.listids.append(int(i))

    # 具体的分析操作
    def analyse(self):
        try:
            self.__get_int_ids()
            with open(self.filePath) as f:
                line = f.readline()
    #            print(line)
                if "log_dirs" in line:
                    line = self.__remove(line)
                    self.__process(line)
                else:
                    self.__process(line)
        except Exception as e:
            print("Exception : ", e)

    # 获取 对应的副本id
    def __get_replica(self):
        random.shuffle(self.listids)
        isr = self.listids[self.index:]
        return isr

    # 获取一个副本
    def __get_ont_replica(self):
        if self.ids is None:
            print("ids must be give..")
        else:
            print("ids = ", self.ids)
            result = self.ids[random.choice(len(self.ids))]
            return result

    # 移除无用的 item
    def __remove(self, content):
        print("__remove content: ", content)
        oneJson = json.loads(content)
        print("version: ", oneJson['version'])
        for itm in oneJson['partitions']:
            del itm['log_dirs']
        print(oneJson)
        return oneJson

    # 得到最终的分配方案
    def __process(self, content):
        print("__process content: ", content)
        for itm in content['partitions']:
            itm['replicas'] = self.__get_replica()
        print("final :",content)

def main():
    fileName = "sourceOne.json"
    # fileName = "sourceMany.json"
    filePath = (BASE+"/"+fileName).replace("\\", "/")
    print("base :", filePath)
    jsonAly = analyseJson(filePath, '1,2,3', 2)
    jsonAly.analyse()


if __name__ == '__main__':
    main()