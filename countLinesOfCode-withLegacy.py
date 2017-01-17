#!/usr/bin/env python3
import os
import functools


def countLines(files):
    for file in files:
        with open(file) as f:
            yield sum(1 for _ in f)


root = './'
for path, subdirs, files in os.walk(root):
    print(sum(countLines(files))
    """for name in files:
        print(countLines(name))
        # print(os.path.join(path, name))
        with open(name) as f:
            # print(len(f.readlines()))
            # print(sum(1 for _ in f))
            sum(1 for _ in f)"""
