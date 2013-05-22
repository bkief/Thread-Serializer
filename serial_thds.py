import threading
from threading import Thread
import time


class ThreadManager:
    def __init__(self):
        self.thread_queue = []
        thm = Thread(target=self.thread_serializer)
        thm.daemon = True
        thm.start()
        

    def thread_serializer(self):
        while True:
            time.sleep(0.1)
            if self.thread_queue:
                th = self.thread_queue[0]
                th.start()
                r = 0
                while th.isAlive():
                    time.sleep(0.25)
                    if r == 0:
                        print "Running"
                        r =1
                    elif r == 1:
                        print "Running."
                        r = 2
                    elif r == 2:
                        print "Running.."
                        r = 3
                    elif r == 3:
                        print "Running..."
                        r = 0
                self.thread_queue.pop(0)
            else:
                pass

        
class Tests:
    def test1(self):
        print 'Test1'
        for i in range(10):
            time.sleep(1)

    def test2(self):
        print 'Test2'
        for i in range(10):
            time.sleep(1)

    def test3(self):
        print 'Test3'
        for i in range(10):
            time.sleep(1)

Tests = Tests()
ThreadManager = ThreadManager()

testThread1 = Thread(target=Tests.test1)
ThreadManager.thread_queue.append(testThread1)
testThread2 = Thread(target=Tests.test2)
ThreadManager.thread_queue.append(testThread2)
testThread3 = Thread(target=Tests.test3)
ThreadManager.thread_queue.append(testThread3)
