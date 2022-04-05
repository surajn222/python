import logging
import threading
import time

def thread_function(name, epoch_time_start, epoch_time_end):
    # logging.info("Thread %s: starting", name)
    # time.sleep(2)
    # logging.info("Thread %s: finishing", name)

    print("Connect to hbase and calculate the number of rows")
    print(epoch_time_start)
    print(epoch_time_end)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()

    epoch_time_start = 0

    for index in range(360):
        logging.info("Main    : create and start thread %d.", index)
        epoch_time_start = epoch_time_start + (index * 3600 * 24)
        epoch_time_end = epoch_time_start + (3600*24)

        x = threading.Thread(target=thread_function, args=(index,epoch_time_start,epoch_time_end))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)