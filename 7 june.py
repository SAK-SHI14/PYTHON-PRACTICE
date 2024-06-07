#OOPS (Object Oriented Programming)
#defining a class
class panda:
    pass
obj = panda()

class Panda:
    attr1 = "mammal"
    def __init__(self, name):
        self.name = name

kungfu = Panda("kungfu")
motu = Panda("motu")

print("kungfu is a {}".format(kungfu.__class__.attr1))
print("motu is a {}".format(motu.__class__.attr1))

print("my name is {}".format(kungfu.name))
print("my name is {}".format(motu.name))

class Base:
    def __init__(self):
        self.a = "futurense"
        self.__c = "futurense"

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("calling private number of base class: ")
       

obj1 = Base()
print(obj1.a)  

obj2 = Derived()


class Person:
    def __init__(self, name, age):
        self.__name = name  
        self.__age = age

    def get_name(self):
        return self.__name

person = Person("sakshi", 18)
print(person.get_name())  

#__str__ method in OOPS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p = Person("sakshi", 18)
print(p)  

#__new__ method in OOPS 
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of MyClass")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing the instance")
        self.name = name

obj = MyClass("sakshi")

#Constructor (__init__ method)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("sakshi", 18)
print(p.name)  
print(p.age)  

#Destructor (__del__ method)
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r")  # Change "s" to "r"

    def __del__(self):
        self.file.close()

fh = FileHandler("example.txt")
del fh