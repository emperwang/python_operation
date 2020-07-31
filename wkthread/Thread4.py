#!/usr/bin/python3
# coding=utf-8
import queue
import threading
import time

exitFlag = 0
class MyThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("start thread :"+self.name)
        process_data(self.name, self.q)
        print("stop thread...."+self.name)


threadList = ["thread-1", "Thread-2", "Thread-3"]
nameList = ["one","two","Three","Four","Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


# 创建线程
for tName in threadList:
    thread = MyThread(threadID,tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1


# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列为空
while not workQueue.empty():
    pass

# 线程退出
exitFlag = 1

# 等待所有线程完成
for i in threads:
    i.join()

print("main stop.")

