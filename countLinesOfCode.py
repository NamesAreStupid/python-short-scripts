#!/usr/bin/env python
import os


def countLines(file):
        try:
            f = open(file)
            return sum(1 for _ in f)
        except Exception as e:
            print("Could not open file: " + str(file))
            # print(e)
            return 0
        else:
            f.close


def listFiles(root):
    """Using a generator expression is less memory intensive than a list comprehension,
    because it yields one item at a time, instead of building a list containing all items.
    """
    for dirpath, dirnames, filenames in os.walk(root):
        for file in filenames:
            yield os.path.join(dirpath, file)


root = 'D:\\'
"""fileList = [os.path.join(dirpath, file)
            for dirpath, dirnames, filenames in os.walk(root)
            for file in filenames]
"""
print(sum(countLines(file) for file in listFiles(root)))
print(list(listFiles(root)))
input("Press any key to continue...")
