#Inheritance

'''
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()
'''

'''
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

'''

'''
class Employee:
    def __init__(self, name, lname):
        self.fullname = name
        self.lastname = lname

    def printname(self):
        print(self.lastname, self.fullname)

class Worker(Employee):
    def __init__(self, name, lname):
        super().__init__(name, lname)

x = Worker("Kam", "Dlubai")
x.printname()

'''

'''
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
'''

#Decorators

'''
def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))
'''

'''
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greep(func):

    greeting = func('Hi, I am created by a function passed as an argument')
    print(greeting)

greep(shout)
greep(whisper)

'''

'''
def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)

print(add_15(10))
'''

def hello_decorator(func):
    def inner1(*args, **kwargs):

        print("before Execution")

        returned_value = func(*args, **kwargs)
        print("after Execution")

        return returned_value

    return inner1


@hello_decorator
def sum_two_numbers(a,b):
    print("Inside the function")

    return a+b

a,b = 1,2

print("Sum =", sum_two_numbers(a, b))

