# Type Code Here
# FUnctions
name = input("enter your name: ")
print("hello, ", name)
      
      
a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a%b)
print(a**b)

print(a>2 and b<2)
print(a>5 or b<8)

Animals = ["panda", "elephant","lion"]
for animal in Animals:
    print(Animals)


    count = 0 
    while count <= 4:
          print (count)
          count +=1    

x= lambda a, b : a*b
print(x(10, 40))

#simple addition 
add_five = lambda x: x + 5
print(add_five(10))  

#string formatting
format_string = lambda name, age: f"Hello, my name is {name} and I am {age} years old."
print(format_string("SAKSHI", 18))

#Sorting a List based on Length
words = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words) 