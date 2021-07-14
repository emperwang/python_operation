# coding=utf-8
# py 2.7
from numpy import *

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataset):
    C1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)

# 数据集   候选集   最小支持度
def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not can in ssCnt.keys():  # ssCnt.has_key(can)
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(LK, k):   # create CK
    retList = []
    lenLK = len(LK)
    for i in range(lenLK):
        for j in range(i+1, lenLK):
            L1 = list(LK[i])[:k-2]
            L2 = list(LK[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(LK[i] | (LK[j]))
    return retList


def apriori(dataset, minSupport = 0.5):
    C1 = createC1(dataset)
    D = map(set, dataset)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while(len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        LK, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(LK)
        k += 1
    return L, supportData


def generateRules(L, supportData, minConf = 0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in  freqSet]
            if i > 1:
                rulesFromConseq(freqSet, H1, supportData,bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData,bigRuleList, minConf)
        return bigRuleList


def calcConf(freqSet, H, supportData, brl, minConf =0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq]
        if conf >= minConf:
            print(freqSet-conseq, '--->', conseq, 'conf', conf)
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m + 1)
        print("Hmp1 = ", Hmp1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        print("calc Hmp1 = ", Hmp1)
        print('len(Hmp1)=', len(Hmp1), 'len(freqSet)=', len(freqSet))
        if (len(Hmp1) > 1):
            print('--------------------', Hmp1)
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)


def testAprior():
    dataSet = loadDataSet()
    print('dataSet=', dataSet)
    # Apriori 算法生成频繁项集以及它们的支持度
    L1, supportData1 = apriori(dataSet, minSupport=0.7)
    print('L(0.7): ', L1)
    print('supportData(0.7):', supportData1)
    print('->'*30)

    # apriori 生成频繁项集以及它们的支持度
    L2, supportData2 = apriori(dataSet, minSupport=0.5)
    print('L(0.5): ', L2)
    print('supportData2(0.5):', supportData2)


def testGenerateRules():
    # 加载测试数据集
    dataSet = loadDataSet()
    print('dataSet : ', dataSet)

    # apriori 算法生成频繁项集以及它们的支持度
    L1, supportData1 = apriori(dataSet, minSupport=0.5)
    print('L(0.5): ', L1)
    print('supportData(0.5)', supportData1)

    # 生成关联规则
    rules = generateRules(L1, supportData1, minConf=0.5)
    print('rules : ', rules)


def test2():
    dd = loadDataSet()
    tt = apriori(dd)
    print(tt)


def test1():
    dd = loadDataSet()
    print("dd= ", dd)
    C1 = createC1(dd)
    print("c1=", C1)
    D = map(set, dd)
    print("d=", D)
    retList, sdata = scanD(D, C1, 0.7)
    print("retlist= ", retList)
    print("sdata = ", sdata)


def main():
    # test1()
    # test2()
    # testAprior()
    testGenerateRules()



if __name__=='__main__':
    main()