def pipeline(numbers, *args):
    x = args[0](numbers)
    for g in args[1:]:
        print(g.__name__)
        x = g(x)
    return x


def addOne(list):
    for i in list:
        print('add 1 to ', i)
        yield i + 1


def square(list):
    for i in list:
        print('square ', i)
        yield i ** 2


def substractOne(list):
    for i in list:
        print('substract 1 ', i)
        yield i - 1


def printer(list):
    for i in list:
        print('print ', i)

numbers = [1, 2, 3, 4, 5]
# pipeline(numbers, addOne, square, substractOne, printer)

mixins = [addOne, square, substractOne, printer]
pipeline(numbers, *mixins)

mixins2 = [addOne, square, substractOne]
piped = list(pipeline(numbers, *mixins2))
print(piped)
