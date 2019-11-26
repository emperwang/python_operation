#!/usr/bin/python3
# coding=utf-8
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("thread starting...")
        print_time(self.name, 5, self.counter)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s"%(threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2,"thread-2", 3)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("exist from main ....")
