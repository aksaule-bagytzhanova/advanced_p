#oop
#class

'''
class Car:

    name = "c200"
    make = "mercedez"
    model = 2008

    def start(self):
        print("Start work")

    def stop(self):
        print("Stop work")

car_a = Car()
car_a.start()
'''


'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
'''

#object
'''
class MyClass:
    x=5

p1 = MyClass()
print(p1.x)
'''

#method
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

'''

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is "+ self.name + "and my age "+ self.age)

p1 = Person("John", 36)

del p1.age
p1.myfunc()

'''
