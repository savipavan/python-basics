# Given a directory path, find out the file name
# having max size recursively

import glob         # ls * or dir *
import os.path      # file path manipulation


def get_max_filename(path):
    def get_files(path, ed={}):  #Since it is recursive, creating nested function #{} empty dict
        files = glob.glob(os.path.join(path, "*"))
        for file in files:
            if os.path.isfile(file):
                ed[file] = os.path.getsize(file)
            else:
                get_files((file, ed))
        return ed
    allfiles = get_files(path) #dict of filename: size
    #sort (asc)that dict based on size
    # sort by key,
    sted = sorted(allfiles, key=lambda k: allfiles[k])
    return sted[-1] if sted else ""     #[-1] is last element

if __name__ == "__main__":
    path = ""
    print(get_max_filename(path))
