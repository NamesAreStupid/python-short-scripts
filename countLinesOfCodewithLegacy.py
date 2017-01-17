#!/usr/bin/env python3
import os


def countLines(file):
        try:
            f = open(file)
            return sum(1 for _ in f)
        except Exception as e:
            print("Error opening file: " + str(file))
            # print(e)
            return 0
        else:
            f.close


def countLinesOld(files):
    for file in files:
        try:
            f = open(file)
            yield sum(1 for _ in f)
        except Exception as e:
            print("Error opening file: " + str(file))
            # print(e)
        else:
            f.close

"""No error handling!"""
def countLinesShort(files):
    for file in files:
        with open(file) as f:
            yield sum(1 for _ in f)


def listFiles(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for file in filenames:
            yield os.path.join(dirpath, file)


def listFilesStrange(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for name in [os.path.join(dirpath, file) for file in filenames]:
            yield name

root = './'
fileList2 = [os.path.join(dirpath, file) for dirpath, dirnames, filenames in os.walk(root) for file in filenames]
print(sum(countLines(file) for file in fileList2))
# fileList = list(listFiles(root))
# linecounts = list(countLinesOld(fileList2))
# print(sum(linecounts))
input("Press any key to continue...")
