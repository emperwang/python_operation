#!/usr/bin/python3
# coding=utf-8
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("starting thread...")
        threadLock.acquire()
        print_time(self.name, 5, self.counter)
        threadLock.release()

threadLock = threading.Lock()
threadRlock = threading.RLock()
threads = []

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s:%s" % (threadName, time.ctime(time.time())))
        counter -= 1

thread1 = MyThread(1, "Thread-1",2)
thread2 = MyThread(1, "Thread-2", 4)

threads.append(thread1)
threads.append(thread2)

thread1.start()
thread2.start()

for i in threads:
    i.join()

print("exist .....")