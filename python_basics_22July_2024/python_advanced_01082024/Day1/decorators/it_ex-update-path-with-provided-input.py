#Given a directory path, prints all files recursively
import glob         # ls * or dir *
import os.path      #file path manipulation
import sys

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


if __name__ == '__main__':
    dpath = r"C:\Windows"
    path = sys.argv[1] if len(sys.argv) > 1 else dpath
    for f in get_files(path):
        print(f)