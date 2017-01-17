#!/usr/bin/env python


def countCoins(amount):
    return cc(amount, 5)


def cc(amount, coinType):
    coinTypes = [1, 5, 10, 25, 50]

    if(amount == 0):
        return 1
    if(amount < 0 or coinType <= 0):
        return 0

    return cc(amount - coinTypes[coinType - 1], coinType) + cc(amount, coinType - 1)


if(__name__ == "__main__"):
    print(countCoins(100))
