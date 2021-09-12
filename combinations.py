def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    print('indices: ' + str(indices))

    while True:
        print('\nStart While:')
        for i in reversed(range(r)):
            print(
                'The formula: indices[{0}](= {3}) != {0} + {1} - {2}'.format(i, n, r, indices[i]))
            if indices[i] != i + n - r:
                print('break')
                break
        else:
            print('else')
            return
        print('i: {}'.format(i))
        indices[i] += 1
        print('j-range({0}, {1})'.format(i + 1, r))
        for j in range(i + 1, r):
            print('j: {}'.format(j))
            indices[j] = indices[j - 1] + 1
        print('indices: ' + str(indices))
        print(tuple(pool[i] for i in indices))
        yield tuple(pool[i] for i in indices)


# print(list(combinations('ABCD', 2)))
# print(list(combinations('ABCD', 2)))
# print(list(combinations('ABCDE', 3)))
print(list(combinations([1, 3, 6, 8, 10, 11], 4)))
