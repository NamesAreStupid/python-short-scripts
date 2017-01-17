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


root = './'
fileList = [os.path.join(dirpath, file)
            for dirpath, dirnames, filenames in os.walk(root)
            for file in filenames]
print(sum(countLines(file) for file in fileList))
input("Press any key to continue...")
