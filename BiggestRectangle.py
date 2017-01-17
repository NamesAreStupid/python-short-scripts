#!/usr/bin/python3



myList = [1,2,3,4,5,6]

print(list(filter(lambda x: x % 2 == 0, myList)))

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)