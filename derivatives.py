#!/usr/bin/env python


def derivative(expression, variable):
    if(isConstant(expression, variable)):
        return 0
    elif(isSameVariable(expression, variable)):
        return 1
    elif(isSum(expression)):
        makeSum(derivative(a1(expression), variable),
                derivative(a2(expression), variable))
    elif(isProduct(expression)):
        makeSum(makeProduct(m1(expression),
                            derivative(m2(expression), variable)),
                makeProduct(derivative(m1(expression), variable),
                            m2(expression)))


def isConstant(expression, variable):
    return isAtomic(expression) and not isEqualTo(expression, variable)


def isSameVariable(expression, variable):
    return isAtomic(expression) and isEqualTo(expression, variable)


def isSum(expression):
    return not isAtomic(expression) and isEqualTo(car(expression), '+')


def isProduct(expression):
    return not isAtomic(expression) and isEqualTo(car(expression), '*')


def isAtomic(expression):
    pass


def isEqualTo(expression, variable):
    pass


def isNumber(variable):
    pass


"""def makeSum(a1, a2):
    return ['+', a1, a2]
"""


def makeSum(a1, a2):
    if(isNumber(a1) and isNumber(a2)):
        return a1 + a2
    elif(isNumber(a1) and a1 == 0):
        a2
    elif(isNumber(a2) and a2 == 0):
        return a1
    else:
        return ['+', a1, a2]


def makeProduct(m1, m2):
    return ['*', m1, m2]


def a1(expression):
    # return cadr(expression)
    return expression[1]


def a2(expression):
    # return caddr(expression)
    return expression[2]


def car(expression):
    pass


def cadr(expression):
    pass


def caddr(expression):
    pass


def m1(expression):
    # return cadr(expression)
    return expression[1]


def m2(expression):
    # return caddr(expression)
    return expression[2]
