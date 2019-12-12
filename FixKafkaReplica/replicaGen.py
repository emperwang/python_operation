#/usr/bin/python3
# encoding=utf-8

import os
import json
import sys
import random

BASE = os.getcwd()


class analyseJson():

    """
     json: 内容是建议分配的json字符串
     ids: kafka 所有有效的broker id
     factor: 副本因子，不可大于broker的数量
    """
    def __init__(self, json, ids, factor):
        self.json = json
        self.ids = ids.split(",")
        self.factor = int(factor)
        if self.factor > len(self.ids):
            print("factor cann't bigger than the num of ids")
            sys.exit(1)
        else:
            self.index = len(self.ids) - self.factor

    # 把字符串都转换为整数
    def __get_int_ids(self):
        self.listids = []
        for i in self.ids:
            self.listids.append(int(i))

    # 具体的分析操作
    def analyse(self):
        try:
            self.__get_int_ids()
            if "log_dirs" in self.json:
                line = self.__remove(self.json)
                self.__process(line)
            else:
                self.__process(self.json)
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
        for itm in oneJson['partitions']:
            del itm['log_dirs']
        print(oneJson)
        return oneJson

    # 得到最终的分配方案
    def __process(self, content):
        print("__process content: ")
        for itm in content['partitions']:
            itm['replicas'] = self.__get_replica()
        print("final :", content)
        final_file = (BASE + "/" + "final.json").replace("\\","/")
        print("final_file path : ", final_file)
        print("json :", json.dumps(content))
        with open(final_file, 'w+') as f:
            f.write(json.dumps(content))


# /mnt/kafka_2.11-2.2.0/bin/kafka-reassign-partitions.sh  --zookeeper name1:2181 --topics-to-move-json-file /mnt/kafka_2.11-2.2.0/bin/topics.json  --broker-list 0,1,2 --generate

def get_json_from_cmd():
    if len(sys.argv) > 2:
        print("cmd_with_path is: ", sys.argv[1])
    else:
        print("Usage : ", sys.argv[0], " cmd_with_path, zk_url, topics_path , ids(like: 0,1,2), factor")
        sys.exit(1)
    return [sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]


def main():
    args = get_json_from_cmd()
    print(args)
    final_cmd = args[1] + " " + " --zookeeper " + args[2]+" --topics-to-move-json-file  "+args[3]+" --broker-list " + args[4] \
                    + " --generate"
    generate_cmd = args[1] + " " + " --zookeeper " + args[2]+" --reassignment-json-file " + BASE +"/" + "final.json" +" --execute"
    print("final cmd :", final_cmd)
    print("execute cmd: ", generate_cmd)
    va = os.popen(final_cmd)
    res = []
    for i in va.read().splitlines():
        print(i)
        res.append(i)
    to_an = res[len(res)-1]
    print("analyse json :", to_an)
    analyse_obj = analyseJson(to_an, args[4], args[5])
    analyse_obj.analyse()
    generate_result = os.popen(generate_cmd)
    gen_result = []
    for re in generate_result.read().splitlines():
        gen_result.append(re)
    print("generate_result :", gen_result)
    rollbackpath = BASE + "/" + "rollback.json"
    with open(rollbackpath,"w+") as back:
        back.write(json.dumps(gen_result[2]))

"""
usage:  第一版本: 还需要指定topics的json文件路径
python replicas.py  
/mnt/kafka_2.11-2.2.0/bin/kafka-reassign-partitions.sh  : 命令全路径
'name1:2181'  : zk url
/mnt/kafka_2.11-2.2.0/bin/topics.json : 要转移的topics  
'0,1,2'     # broker ids
2           # 副本因子
"""
"""

"""

if __name__ == '__main__':
    main()