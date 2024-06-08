#INHERITENCE IN PYTHON:
class Bird:
  def make_sound(self):
    print("Generic bird sound")

class Parrot(Bird):
  def make_sound(self):
    print("Squawk!")

class Sparrow(Bird):
  def make_sound(self):
    print("Chirp!")

class Falcon(Bird):
  def make_sound(self):
    print("Screech!")

class AfricanGreyParrot(Parrot):  # AfricanGreyParrot inherits from Parrot
  pass

birds = [Bird(), Parrot(), Sparrow(), Falcon(), AfricanGreyParrot()]
for bird in birds:
  bird.make_sound()

  #single inheritence:
  # Parent class
class Vehicle:
  def __init__(self, brand, year):
    self.brand = brand
    self.year = year

  def info(self):
    print(f"Brand: {self.brand}, Year: {self.year}")

# Child class inherits from Vehicle
class Car(Vehicle):
  def __init__(self, brand, year, doors):
    super().__init__(brand, year)
    self.doors = doors

  def car_info(self):
    self.info()
    print(f"Doors: {self.doors}")

# Create an instance of Car
my_car = Car("Toyota", 2022, 4)

# Call the methods
my_car.car_info()


#multiple inheritence:
# Parent class 1
class Flyable:
  def fly(self):
    print("I can fly!")

# Parent class 2
class Mammable:
  def make_sound(self):
    print("I can make a sound!")

# Child class inherits from Flyable and Mammable
class Bird(Flyable, Mammable):
  def __init__(self, name):
    self.name = name

  def introduce(self):
    print(f"Hello, I'm a {self.name}!")

# Create an instance of Bird
my_bird = Bird("Sparrow")

# Call the methods
my_bird.introduce()
my_bird.fly()
my_bird.make_sound()

#multilevel inheritence:
# Grandparent class
class Animal:
  def eat(self):
    print("I can eat!")

# Parent class inherits from Animal
class Mammal(Animal):
  def walk(self):
    print("I can walk!")

# Child class inherits from Mammal
class Dog(Mammal):
  def bark(self):
    print("I can bark!")

# Create an instance of Dog
my_dog = Dog()

# Call the methods
my_dog.eat()
my_dog.walk()
my_dog.bark()


#Hierarchical Innheritance :
# Parent class
class Animal:
  def eat(self):
    print("I can eat!")

# Child class 1 inherits from Animal
class Dog(Animal):
  def bark(self):
    print("I can bark!")

# Child class 2 inherits from Animal
class Cat(Animal):
  def meow(self):
    print("I can meow!")

# Create instances of Dog and Cat
my_dog = Dog()
my_cat = Cat()

# Call the methods
my_dog.eat()
my_dog.bark()
my_cat.eat()
my_cat.meow()

# Hybrid Inheritance :
# Parent class 1
class A:
  def method_A(self):
    print("This is method A")

# Parent class 2
class B:
  def method_B(self):
    print("This is method B")

# Child class 1 inherits from A
class C(A):
  def method_C(self):
    print("This is method C")

# Child class 2 inherits from B and C (Hybrid Inheritance)
class D(B, C):
  def method_D(self):
    print("This is method D")

# Create an instance of D
my_D = D()

# Call the methods
my_D.method_A()
my_D.method_B()
my_D.method_C()
my_D.method_D()


#method overriding:
# Parent class
class Animal:
  def sound(self):
    print("The animal makes a sound.")

# Child class that overrides the sound method
class Dog(Animal):
  def sound(self):
    print("The dog barks.")

# Child class that overrides the sound method
class Cat(Animal):
  def sound(self):
    print("The cat meows.")

# Create instances of Dog and Cat
my_dog = Dog()
my_cat = Cat()

# Call the overridden methods
my_dog.sound()
my_cat.sound()

#super() method:
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print(self.name, self.id)

class Emp(Person):
    def __init__(self, name, id):
        self.name_ = name
        super().__init__(name, id)

    def Print(self):
        print("Emp class called")

Emp_details = Emp("Mayank", 103)
print(Emp_details.name_, Emp_details.name)

#Super() with __init__ method :
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)  
        self.age = age

    def sound(self):
        print("The dog barks.")

my_dog = Dog("Fido", 3)
print(my_dog.name)  
print(my_dog.age) 
my_dog.sound()      

#Super() with __str__ method :
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return f"{super().__str__()} - Age: {self.age}"

my_dog = Dog("Fido", 3)
print(my_dog)  



#EXCEPTION HANDLING :
try:
    x = 55
    y = 0
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

#handling multiple exceptions:
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("The result is: ", result)

except (ValueError, ZeroDivisionError):
    print("Error: Invalid input or division by zero.")

except Exception as e:
    print("An unexpected error occurred: ", str(e))

finally:
    print("Thanks for using our program!")
       

#Using else and finally blocks:
try:
    a = int(input())
    b = int(input())
    result = a/b
    print(result)

except:
    print("We caught an error")

else:
    print("Hurray, we don't have any errors")

finally:
    print("I have reached the end of the line")


#COMMON BUILT-IN EXCEPTIONS:
#syntax error:
try:
    compile('invalid syntax', '<string>', 'exec')  # This will raise a SyntaxError
except SyntaxError:
    print("Error: Invalid syntax.")

#intendation error
try:
    compile("""
def hello
    print("Hello World")
    """, '<string>', 'exec')  # This will raise an IndentationError
except IndentationError:
    print("Error: Invalid indentation.")

#name error:
try:
    x = y + 2  # This will raise a NameError
except NameError:
    print("Error: Variable is not defined.")

#type error:
try:
    a = "hello"
    b = 5
    c = a(b)  # This will raise a TypeError
except TypeError:
    print("Error: 'str' object is not callable.")

#value error
try:
    int("hello")  # This will raise a ValueError
except ValueError:
    print("Error: Invalid literal for int().")

#zero division error
numerator = 10
denominator = 0

try:
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")    

#custom exceptions 
python
class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong")
except MyError as e:
    print("Error:", e)

#Using except with specific exception
python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#Using as to get exception details
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")

#Raising Exceptions in Python:    
try:
    raise ConnectionError
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc