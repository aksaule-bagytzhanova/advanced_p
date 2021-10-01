# reduce(fun,seq)
'''
import functools

lis = [1,3,5,6,2]

print("The sum of the list elements is :  ", end='')
print(functools.reduce(lambda a,b: a+b, lis))

'''

'''
import functools
import operator

lis = [1,3,5,6,2]

print("The sum of the list elements is : ", end = "")
print(functools.reduce(operator.add, lis))

print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))
'''
