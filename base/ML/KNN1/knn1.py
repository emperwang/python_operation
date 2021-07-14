#!/bin/env python
# coding=utf-8
# py 2.7
from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    # 获取 维度
    dataSetSize = dataSet.shape[0]
    # 对输入的要检测是护具 inX 进行维度的扩充
    # - dataSet 操作 是求节点间的 差值
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # 差值平方
    sqDiffMat = diffMat ** 2
    # 相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方
    distances = sqDistances ** 0.5
    # 获取distance中数据的排序后的 index的值，从小到大
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 获取前k个值，此时KNN的来源
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 返回最相近的第一个值
    return sortedClassCount[0][0]


if __name__=='__main__':
    group, labes = createDataSet()
    dd = classify0([0, 0], group, labes, 3)
    print(dd)
