'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
        print("And my age is " + str(self.age))

p1 = Person("John", 36)
p1.age = 40
p1.myfunc()

p2 = Person("Aksi", 20)
p2.myfunc()
'''

#Python Inheritance
'''
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()


class Student(Person):
    pass

x = Student("Mike", "Olsen")
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
    def __init__(self, t_name):
        self.teacher_name = t_name

    def printname_all(self):
        print(self.teacher_name)

x = Student("Doe")
x.printname_all()
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
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradutionyear = year

    def welcome(self):
        print("Welcome", self.firstname,
              self.lastname, "to the class of",
              self.gradutionyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
'''


#Iterator

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))