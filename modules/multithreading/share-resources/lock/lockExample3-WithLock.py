import logging
import threading
from threading import Lock
import time

def thread_execution_function(index, lock):
    #append to file
    print("writing to fle")
    lock.acquire()
    file = open("thread-lock-example", "a")
    file.write(str(index))
    file.close

    lock.release()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

    lock = Lock()

    threads = list()

    for index in range(100):
        logging.info("This thread will open a file and write a number to it")

        x = threading.Thread(target=thread_execution_function, args=(index,lock))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    file = open("thread-lock-example", "a")
    file.write("\n")
    file.close


    file = open("thread-lock-example", "r")
    contents = file.read()
    print(contents)
