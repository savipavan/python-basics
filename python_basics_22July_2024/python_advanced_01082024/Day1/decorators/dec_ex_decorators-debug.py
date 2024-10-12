#Given a directory path, find out the file name
#having max size  recursively 

"""
decorator 
    enhancing existing functionality
    a function taking another function return other function 

case-1
    comment out @profile
    result : No debug output
case-2
    with @profile, but comment out print(get_max_filename(path))
    output:
        profile:called <function get_max_filename at 0x0000025E6F6E4D60>
         profile:returned <function profile.<locals>._inner at 0x0000025E6F9DA480>
        _inner:called ('.',) {}
        Time taken 0.0010173320770263672 secs
        _inner:returned
        .\dec_ex_decorators-debug.py
case-3
    uncomment all
        output:
        profile:called <function get_max_filename at 0x0000025E6F6E4D60>
         profile:returned <function profile.<locals>._inner at 0x0000025E6F9DA480>
        _inner:called ('.',) {}
        Time taken 0.0010173320770263672 secs
        _inner:returned
        .\dec_ex_decorators-debug.py


decorator can stack
decorator take arguments
    function taking arg returning function which takes function returns function

Decorators can be used in day today work

"""
DEBUG = True
def d_print(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

import glob  # ls * or dir *
import os.path  #file path manipulation
import time

def profile(func):  #func=get_max_filename
    d_print("profile:called", func)

    def _inner(*args, **kwargs):  #args = (path,) kwargs={} #4
        d_print("_inner:called", args, kwargs)
        st = time.time()
        res = func(*args, **kwargs)  #get_max_filename(path) #5
        print("Time taken", time.time() - st, "secs")
        d_print("_inner:returned")
        return res

    d_print("profile:returned", _inner)
    return _inner


@profile
@profile  #get_max_filename=profile(get_max_filename)= _inner #1
def get_max_filename(path):
    def get_files(path, ed={}):  #ed default arg, #{} - empty dict 
        files = glob.glob(os.path.join(path, "*"))
        for file in files:
            if os.path.isfile(file):
                ed[file] = os.path.getsize(file)
            elif os.path.isdir(file):
                get_files(file, ed)
        return ed

    allfiles = get_files(path)  # dict of filename: size  # 5
    #sort (asc) that dict based on size/value, 
    #sort by key , 
    sted = sorted(allfiles, key=lambda filename: allfiles[filename])
    return sted[-1] if sted else ''
    #last element =-1 


if __name__ == '__main__':
    path = r""
    print(get_max_filename(path))  #_inner(path) #2
