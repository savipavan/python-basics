# Given a directory path, find out the file name
# having max size recursively


"""
decorator:
    enhancing existing functionality
    a function taking another function return other function
"""
import glob         # ls * or dir *
import os.path      # file path manipulation
import time

def get_max_filename(path):
    def get_files(path, ed={}):  #Since it is recursive, creating nested function #{} empty dict
        files = glob.glob(os.path.join(path, "*"))
        for file in files:
            if os.path.isfile(file):
                ed[file] = os.path.getsize(file)
            else:
                get_files((file, ed))
        return ed
    st = time.time()
    allfiles = get_files(path) #dict of filename: size
    #sort (asc)that dict based on size
    # sort by key,
    sted = sorted(allfiles, key=lambda k: allfiles[k])
    print("Time taken", time.time()-st, "secs")
    return sted[-1] if sted else ""     #[-1] is last element

if __name__ == "__main__":
    path = ""
    print(get_max_filename(path))
