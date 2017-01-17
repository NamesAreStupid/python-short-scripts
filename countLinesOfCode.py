#!/usr/bin/env python3
import os


def countLines(files):
    for file in files:
        with open(file) as f:
            yield sum(1 for _ in f)


root = './'
for path, subdirs, files in os.walk(root):
    print(sum(countLines(files)))

input("Press any key to continue...")