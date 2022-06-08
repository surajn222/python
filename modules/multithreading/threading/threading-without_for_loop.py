import logging
import threading
import time
from threading import Lock

lock = Lock()
def thread_function(name, epoch_time_start, epoch_time_end):
    # logging.info("Thread %s: starting", name)
    # time.sleep(2)
    # logging.info("Thread %s: finishing", name)

    print("Connect to hbase and calculate the number of rows")
    print(epoch_time_start)
    print(epoch_time_end)


def thread_function_1(lock):
    # logging.info("Thread %s: starting", name)
    # time.sleep(2)
    # logging.info("Thread %s: finishing", name)
    for i in range(10):
        lock.acquire()
        print("thread1")
        time.sleep(1)
        lock.release()


def thread_function_2(lock):
    # logging.info("Thread %s: starting", name)
    # time.sleep(2)
    # logging.info("Thread %s: finishing", name)
    for i in range(10):
        lock.acquire()
        print("thread2")
        time.sleep(1)
        lock.release()

def thread_function_3(lock):
    # logging.info("Thread %s: starting", name)
    # time.sleep(2)
    # logging.info("Thread %s: finishing", name)
    for i in range(10):
        lock.acquire()
        print("thread3")
        time.sleep(1)
        lock.release()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

    epoch_time_start = 0

    t1 = threading.Thread(target=thread_function_1, args=(lock,))
    t1.start()

    t2 = threading.Thread(target=thread_function_2, args=(lock,))
    t2.start()

    t3 = threading.Thread(target=thread_function_3, args=(lock,))
    t3.start()

    t1.join()
    t2.join()
    t3.join()
