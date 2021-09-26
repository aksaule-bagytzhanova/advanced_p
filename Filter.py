'''

def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = filter(fun, sequence)

print('The filtered letters are: ')
for s in filtered:
    print(s)

'''

'''
a = [-1, 0, 1, 0, 0, 1, 0, -1]
b = list(filter(None,a))
print(b)
'''

'''
s = ['a', '', 'd', 'cc', '']
ss = list(filter(None, s))
print(ss)
'''

'''
numbers = [1,2,3,4,5,6,7]

def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

our_filter = filter(filter_odd_num, numbers)

print("Type object our_filter: ", type(our_filter))
print("Onfiltered list: ", list(our_filter))
'''