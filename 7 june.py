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

person = Person("sakshi", 30)
print(person.get_name())  # John