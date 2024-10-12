##################it_ex.py
#Given a directory path, prints all files recursively
import glob         # ls * or dir *
import os.path      #file path manipulation
import sys

#eager computation
def get_files(path, lst=None):
    if lst is None:
        lst = []
    files = glob.glob(os.path.join(path, "*"))
    for file in files:
        if os.path.isfile(file):
            lst.append(file)
        elif os.path.isdir(file):
            get_files(file, lst)
    return lst

#Iterator - handling infinite data - lazy computation
def get_files_it(path):
    files = glob.glob(os.path.join(path, "*"))
    for file in files:
        if os.path.isfile(file):
            yield file
        elif os.path.isdir(file):
            yield from get_files_it(file)

#OOP based Iterator
class Files:
    def __init__(self, path):
        self.path = path
    def __iter__(self):
        files = glob.glob(os.path.join(self.path, "*"))
        for file in files:
            if os.path.isfile(file):
                yield file
            elif os.path.isdir(file):
                yield from Files(file)


if __name__ == '__main__':
    dpath = r"C:\Windows"
    path = sys.argv[1] if len(sys.argv) > 1 else dpath
    for f in Files(path):
        print(f)


"""
range(010), enumerate dir(itertools) are iterators


################PROMPT
>>> def f():
    ...     yield 1
...     yield 2
...     yield 3
...
>>> i = iter(f())
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
>>> next(i)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
>>> lst = [1,2,3]
>>> i = iter(lst)
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
>>> next(i)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
>>> #User level -iterator - for
>>> for e in f():
    ...     print(e)
...
1
2
3
>>> #for-calls iter, then next, then StopIteration
>>>
>>> #for-calls iter, then next, then StopIteration
>>> range(10)
range(0, 10)
>>> zip
<class 'zip'>
>>> enumerator
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'enumerator' is not defined
>>> enumerate
<class 'enumerate'>
>>> import itertools
>>> dir(itertools)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', '_grouper', '_tee', '_tee_dataobject', 'accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'filterfalse', 'groupby', 'islice', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee', 'zip_longest']
>>> #Refer - https://docs.python.org/3/library/index.html
"""