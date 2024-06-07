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

#Constructor without arguments
class Person:
    def __init__(self):
        self.name = "sakshi"
        self.age = 18

p = Person()
print(p.name)  
print(p.age) 

#Constructor with arguments
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("sakshi", 18)
print(p.name)  
print(p.age)  

 #Constructor with default arguments
class Person:
    def __init__(self, name, age=18, state="PUNJAB"):
        self.name = name
        self.age = age
        self.state = state

p1 = Person("sakshi")
print(p1.name)  
print(p1.age)  
print(p1.state)  

p2 = Person("Jane", 18, "PUNJAB")
print(p2.name)  
print(p2.age)  
print(p2.state)  

#Pass object as an argument
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def greet(person):
    print(f"Hello, {person.name}! You are {person.age} years old.")

john = Person("sakshi", 18)
greet(sakshi) 


#Object as an return type
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def create_points(x1, y1, x2, y2)
    

#Method overloading
def add_numbers(x, y):
    return x + y

def add_strings(x, y):
    return x + y

print(add_numbers(5, 3))   
print(add_strings("Hello", " World")) 

#data handling 
# List Example
fruits = ['apple', 'banana', 'cherry']

# Accessing list elements
print(fruits[0])  

# Modifying list elements
fruits[1] = 'orange'
print(fruits)  

# Appending to a list
fruits.append('grape')
print(fruits)  

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private instance variable
        self.__age = age  # Private instance variable

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):"
    if new_age >= 0:
            self.__age = new_age
    else:
        print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("sakshi", 18)

# Calling the getter methods
print("Name:", person.get_name())
print("Age:", person.get_age())

# Calling the setter method
person.set_age(30)
# Calling the getter method again
print("Updated Age:", person.get_age())