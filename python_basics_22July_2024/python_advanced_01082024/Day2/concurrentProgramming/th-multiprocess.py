'''
3 techniquies:
- Single host, Single process, multi-threads
    threading - module name
- Single host, multiprocess
    multiprocessing - module name
- Multihost(also called cluster computation) - eg. pySpark required dedicated framework and need more hosts
cluster computation workds on mapReduce paradiagm,
    pySpark = MapReduce
    Map - Multihost element trx
    Reduce - summerization of all data from Map hosts
    pySpark is complicated framework need to know map, reduce

joblib:
    - thread or process with config

Thread - is lightweight
    - In single process many threads can be run
    - All share one process constraint
    - in process, one python code can be interpreted - GIL
    - GIL is common in interpreted language - Valid cPython type compiler, similar Iron Python, Jython

process - is heavyweight

# to create a process we need memory allocation

first process - MainProcess
'''

import threading
import time

def worker(sleeptime):
