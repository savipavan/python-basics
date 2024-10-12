import glob         # ls * or dir *
import os.path      #file path manipulation
import time

def profile(func):      #func=get_max_filename
    def _inner(*args, **kwargs):        #args = (path, kwargs={}    #4
        st = time.time()
        res = func(*args, **kwargs)     # here it main function is calling #5
        print("Time taken", time.time()-st, "secs")
        return res
    return _inner


@profile                #get_max_filename=profile(get_max_filename) ==inner #1
def get_max_filename(path):
    def get_files(path, ed={}):  #ed default arg, #{} - empty dict
        files = glob.glob(os.path.join(path, "*"))
        for file in files:
            if os.path.isfile(file):
                ed[file] = os.path.getsize(file)
            elif os.path.isdir(file):
                get_files(file, ed)
        return ed
    allfiles = get_files(path) # dict of filename: size     # 5
    #sort (asc) that dict based on size/value,
    #sort by key ,
    sted = sorted(allfiles, key=lambda filename: allfiles[filename])
    return sted[-1] if sted else ''
    #last element =-1

if __name__ == '__main__':
    path = r""
    print(get_max_filename(path))