########################th.py
"""
Single host, Single process, multi threads
    threading

Single host, multi process
    multiprocessing

Multihost - cluster computation
    pyspark - MapReduce
    Map - multihost element trx
    Reduce - summerization of all data from Map hosts

joblib
    thread or process with config

Thread
    light wts , in process, many threads can be run
    all share one process constraint
    GIL - valid Cpython
    https://docs.python.org/3/library/threading.html
    Iron python, jython(java) - GIL constraints
    IO bound - Networking ops-GIL is released
    numpy ops - GIL is released

    first thread - MainThread

Process
    heavy wt
    application CPU bound

    first process(OS) - MainProcess

Synchronization

https://docs.python.org/3/library/threading.html
https://docs.python.org/3/library/multiprocessing.html

"""
import threading
import time


def worker(sleeptime):
    print(threading.current_thread().name, "entering")
    time.sleep(sleeptime)
    print(threading.current_thread().name, "exiting")


if __name__ == '__main__':
    print("Sequentially")
    worker(5)
    print("parallel")
    st = time.time()
    ths = []
    for i in range(10):
        th = threading.Thread(target=worker, args=(5,))
        ths.append(th)
    #start it after creation
    [th.start() for th in ths]
    #wait for end - join
    [th.join() for th in ths]
    print("Time Taken", time.time()-st, "secs")
