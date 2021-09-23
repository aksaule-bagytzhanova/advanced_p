'''
def pure_func(List):

    New_List = []

    for i in List:
        New_List.append(i**2)

    return New_List

Original_List = [1,2,3,4]
Modified_List = pure_func(Original_List)

print("Original List:", Original_List)
print("Modified List:", Modified_List)

'''


'''
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):

    greeting = func("Hi, I am created by a function as an argument.")
    print(greeting)

greet(shout)
greet(whisper)

'''


def addition(n):
    return n+n

numbers = (1, 2, 3, 4)
results = map(addition, numbers)

print(results)

for result in results:
    print(result, end= " ")







