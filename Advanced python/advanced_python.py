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


#dunder

#init
'''
class softwares:
    names = []
    versions = {}

    def __init__(self, names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Please Enter the ")

'''
#easy python code
'''
p = softwares(['S1','S2','S3'])
p1 = softwares([])
'''

#str
'''
def __str__(self):

    s="The current softwares and their versions are listed below: \n"
    for key,value in self.versions.items():
        s+= f"{key} : v{value} \n"
    return s

'''

#easy python code
#print(p)

#setitem

'''
d = {}
d['key'] = value

def __setitem__(self,name,version):
    if name in self.versions:
        self.versions[name] = version
    else:
        raise Exception("Software Name doesnt exist")

'''
#str
'''
p['S1'] = 2
p['2'] = 2
'''

#getitem

'''
d = {'val':key}
print(d['val'])

def __getitem__(self, name):
    if name in self.versions:
        return self.versions[name]
    else:
        raise Exception("Software Name doesn't exist")
'''

#str
'''
print(p['S1'])
print(p['1'])

'''

#delitem

'''
def __delitem__(self,name):
    if name in self.versions:
        del self.versions[name]
        self.names.remove(name)
    else:
        raise Exception("Software Name doesn't exist")
    
'''

#str
# del p['S1']


#len
'''
def __len__(self):
    return len(self.names)
'''


#print(len(p))

#contains
'''
def __contains__(self, name):
    if name in self.versions:
        return True
    else:
        return False

'''

'''
if 'S2' in p:
    print("Software Exists")
else:
    print("Software DOESN'T exist")

'''