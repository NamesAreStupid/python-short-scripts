#!/usr/bin/env python


def isertionSort(a):
    for j in range(1, len(a)):
        key = a[j]
        # Insert A[j] into the sorted sequence A[1..j-1]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a


a1 = [5, 2, 4, 6, 1, 3]
# print(isertionSort(a1))


def merge(a, p, q, r):
    print("MERGE")
    print("a: ", a)
    n1 = q - p + 1
    n2 = r - q
    # print("n1 = ", n1, ",  n2 = ", n2)
    left = [None] * (n1 + 1)
    # print(len(left))
    right = [None] * (n2 + 1)
    # print(len(right))
    for i in range(0, n1):
        left[i] = a[p + i - 1]
    for j in range(0, n2):
        right[j] = a[q + j]
    sentinel = max(a) + 1
    print("sentinel: ", sentinel)
    left[n1] = sentinel
    print("left+sen: ", left)
    right[n2] = sentinel
    print("right+sen: ", right)
    i = 1
    j = 1
    for k in range(p, r):
        if(left[i] <= right[j]):
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
    print("merged: ", a)
    return a


def mergeSort(a, p, r):
    print("MERGE-SORT")
    print("a: ", a[p: r + 1])
    if(p < r):
        q = int((p + r) / 2)
        # print("p: ", p, "q: ", q, "r: ", r)
        print("left: ", a[p: q + 1])
        mergeSort(a, p, q)
        print("right: ", a[(q + 1): r + 1])
        mergeSort(a, q + 1, r)
        return merge(a, p, q, r)


a2 = [2, 4, 5, 7, 1, 2, 3, 6]
merged = mergeSort(a2, 0, 7)
print("merged: ", merged)