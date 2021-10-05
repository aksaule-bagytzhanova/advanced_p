# map() function return a map object(which is an iterator)
# of the results after applying the given func
# to each item of a given iterable (list, tuple, etc)

# map(fun, item)

'''

def addition(n):
    return n+n

numbers = (1,2,3,4)
result = map(addition, numbers)
print(list(result))

'''


'''
numbers = (1,2,3,4)
result = map(lambda x: x+x, numbers)
print(list(result))
'''

'''
numbers1 = [1,2,3]
numbers2 = [4,5,6]

result = map(lambda x,y: x+y, numbers1, numbers2)

print(list(result))

'''

'''
list_of_words = ['one','two','list']

result = list(map(str.upper, list_of_words))
print(result)
'''


#List comprehension вместо map

list_of_words = ['one', 'two', 'list']

list_of_words = [word.upper() for word in list_of_words]
print(list_of_words)