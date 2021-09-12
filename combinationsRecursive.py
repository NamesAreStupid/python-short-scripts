# def combinationsRecursive(iterable, r):
#     for i, e in enumerate(iterable[:len(iterable) - r]):
#         print(e)
#         for test in combinationsRecursive(iterable[(i + 1):(len(iterable) - (r - 1))], (r - 1)):
#             yield list(e, test)


# def combinationsRecursive(iterable, r):
#     combinations = []
#     if(r == 1):
#         for e in iterable:
#             combinations.append([e])
#         return combinations
#     for i in range(len(iterable) - (r - 2)):
#         for comb in combinationsRecursive(iterable[i:], r - 1):
#             combinations.append([i].append(comb))
#     return combinations


# print(combinationsRecursive([1, 3, 6, 8, 10, 11], 3))


# def combinationsRecursive(iterable, r):
#     print('combinationsRecursive: {0}, {1}'.format(iterable, r))
#     # print(iterable)
#     # print(r)
#     combinations = []
#     remaining = r - 2
#     # print(len(iterable) - r + 1)
#     if(r == 1):
#         # print('if: {0}'.format(iterable))
#         for e in iterable:
#             combinations.append([e])
#         # print('combinations from if: {0}'.format(combinations))
#         return combinations
#     for i in range(len(iterable) - r + 1):
#         # print('for: {0}'.format(iterable))
#         # print(i)
#         # print(iterable[i+1:])
#         for e in combinationsRecursive(iterable[i + 1:], r - 1):
#             # print('That e: {0}'.format(e))
#             # tmpList = [iterable[i].append(e)]
#             # print('The type: {0}'.format(type(e)))
#             tmpList = [iterable[i]]
#             tmpList.extend(e)
#             # print('tmpList: {0}'.format(tmpList))
#             combinations.append(tmpList)
#         # combinations.append(combinationsRecursive(iterable[i+1:], r - 1))
#         # print(combinationsRecursive(iterable[i+1:], r - 1).insert(0, iterable[i]))
#         # combinationsRecursive(iterable[i+1:], r - 1)
#     return combinations

def combinationsRecursive(iterable, r):
    # print('combinationsRecursive: {0}, {1}'.format(iterable, r)) # This shows the potential for Dynamic Programming to avoid redundant execution
    combinations = []
    if(r == 0 or r > len(iterable)):
        return combinations
    if(r == 1):
        for e in iterable:
            combinations.append([e])
        return combinations
    r = r - 1
    for i in range(len(iterable) - r):
        for e in combinationsRecursive(iterable[i + 1:], r):
            tmpList = [iterable[i]]
            tmpList.extend(e)
            combinations.append(tmpList)
    return combinations


from math import *
combs = combinationsRecursive([1, 3, 6, 8, 10, 11], 3)
print(combs)
print(len(combs))
print(factorial(6) / factorial(3) / factorial(6 - 3))
print(list([1]).append(2))
