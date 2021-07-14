#!/usr/bin/python
# coding:utf-8
import sys
import getopt


def useoptParam():
    """
    通过opt模块获取命令行参数
    :return:
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o", ["ifile=", "ofile="])
        # print(opts)
        # print(args)
    except getopt.GetoptError:
        print("{} -i <inputfile> -o <outputfile>".format(sys.argv[0]))
        sys.exit(2)
    for opt, arg in opts:
        # print("opt = {}, arg = {}".format(opt, arg))
        if opt == 'h':
            print("{} -i <inputfile> -o <outputfile>".format(sys.argv[0]))
        elif opt in ("-i", "-ifile"):
            print("input file is:{}".format(arg))
        elif opt in ("-o", "-ofile"):
            print("output file is:{}".format(arg))
        else:
            print("{} -i <inputfile> -o <outputfile>".format(sys.argv[0]))


if __name__ == '__main__':
    useoptParam()
