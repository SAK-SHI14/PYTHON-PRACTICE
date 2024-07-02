#LISTS IN PYTHON:
# Create a list
my_list = [1, 2, 3, 4, 5]

# Append
my_list.append(6)
print("After append:", my_list)

# Insert
my_list.insert(2, 7)
print("After insert:", my_list)

# Remove
my_list.remove(4)
print("After remove:", my_list)

# Shallow copy
shallow_copy = my_list.copy()
print("Shallow copy:", shallow_copy)

# Deep copy
import copy
deep_copy = copy.deepcopy(my_list)
print("Deep copy:", deep_copy)

# Counting
print("Count of 2:", my_list.count(2))

# Extending
my_list.extend([8, 9, 10])
print("After extend:", my_list)

# Indexing
print("Element at index 3:", my_list[3])

# Sorting
my_list.sort()
print("After sort:", my_list)

# Reversing
my_list.reverse()
print("After reverse:", my_list)

# Clearing
my_list.clear()
print("After clear:", my_list)

# Popping
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(2)
print("Popped element:", popped_element)
print("After pop:", my_list)

#slicing in lists
#positive slicing
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[1:5]) 
print(nums[1:])  
print(nums[:5]) 

#negative slicing
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[-3:])  
print(nums[-5:-1])  

#retreiving
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[1])  
print(nums[-1]) 

#updating 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
nums[1:5] = [1, 2, 3, 4]
print(nums)  

#deleting
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
del nums[1:5]
print(nums)  

#inserting
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
nums[1:1] = [1, 2, 3]
print(nums)  

#searchimg in lists
#linear search
def linear_search(list, objective):
    for i in range(len(list)):
        if list[i] == objective:
            return i
    return -1

list = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
objective_number = 39
result = linear_search(list, objective_number)

if result != -1:
    print(f"The number {objective_number} is located at position: {result}")
else:
    print(f"The number {objective_number} is NOT in the list")

#binary search
def binary_search(list, objective):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == objective:
            return mid
        elif list[mid] < objective:
            low = mid + 1
        else:
            high = mid - 1
    return -1

list = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
objective_number = 39
result = binary_search(list, objective_number)

if result != -1:
    print(f"The number {objective_number} is located at position: {result}")
else:
    print(f"The number {objective_number} is NOT in the list")

#sorting in lists
def insertion_sort(unordered_list):
    for i in range(1, len(unordered_list)):
        next_element = unordered_list[i]
        j = i - 1
        while (unordered_list[j] > next_element) and (j >= 0):
            unordered_list[j + 1] = unordered_list[j]
            j = j - 1
        unordered_list[j + 1] = next_element
    return unordered_list

unordered_list = [7, 2, 1, 6]
print("The unsorted list is:", unordered_list)
print("The sorted new list is:", insertion_sort(unordered_list))

#bubble sort
def bubble_sort(unordered_list):
    for num in range(len(unordered_list) - 1, 0, -1):
        for idx in range(num):
            if unordered_list[idx] > unordered_list[idx + 1]:
                temp = unordered_list[idx]
                unordered_list[idx] = unordered_list[idx + 1]
                unordered_list[idx + 1] = temp
    return unordered_list

unordered_list = [7, 2, 1, 6]
print("The unsorted list is:", unordered_list)
print("The sorted new list is:", bubble_sort(unordered_list))


#practice questions
fruits = ["apple", "banana", "cherry", "date"]

# Add a new fruit "fig" to the end of the list
fruits.append("fig")
print("Q1.1 - After appending 'fig':", fruits)

# Insert "grape" at the 2nd position (index 1)
fruits.insert(1, "grape")
print("Q1.2 - After inserting 'grape' at index 1:", fruits)

# Remove the first occurrence of "banana"
fruits.remove("banana")
print("Q1.3 - After removing 'banana':", fruits)

# Return the first and last element of the list
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("Q1.4 - First and last fruit:", first_fruit, last_fruit)

#question2
fruits = ["apple", "grape", "cherry", "date", "fig"]

# Get the third fruit from the list
third_fruit = fruits[2]
print("Q2.1 - Third fruit:", third_fruit)

# Retrieve a slice containing the first three fruits
first_three_fruits = fruits[:3]
print("Q2.2 - First three fruits:", first_three_fruits)

# Retrieve a slice containing the last two fruits using negative indexing
last_two_fruits = fruits[-2:]
print("Q2.3 - Last two fruits:", last_two_fruits)

# Update the second fruit to "blueberry"
fruits[1] = "blueberry"
print("Q2.4 - After updating the second fruit:", fruits)

#question 3
#append() 
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("After appending 6:", numbers)  

#insert()
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 0)
print("After inserting 0 at the beginning:", numbers)  

#pop()
numbers = [1, 2, 3, 4, 5]
last_element = numbers.pop()
print("Last element popped:", last_element, "Remaining list:", numbers)  

#count()
numbers = [1, 2, 2, 3, 4, 5]
count_2 = numbers.count(2)
print("Count of '2':", count_2)  

#indexing()
numbers = [1, 2, 3, 4, 5]
index_3 = numbers.index(3)
print("Index of '3':", index_3) 

#reverse()
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print("After reversing:", numbers)  

#question 4 
#Creating a list of even numbers
even_numbers = [x for x in range(21) if x % 2 == 0]
print("Even numbers:", even_numbers)  

#Creating a list of squares of numbers
squares = [x ** 2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)  

#. Creating a list of uppercase words
words = ["hello", "world", "python", "lists"]
uppercased = [word.upper() for word in words]
print("Uppercased words:", uppercased)  

# Creating a flattened list from a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print("Flattened list from nested list:", flattened) 

#question5
# Checking if an element is in the list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
has_cherry = "cherry" in fruits
print("Q5.1 - Is 'cherry' in the list?", has_cherry) 

#Finding the index of an element in the list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
date_index = fruits.index("date")
print("Q5.2 - Index of 'date':", date_index) 

#Sorting the list in ascending order
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits.sort()
print("Q5.3 - Fruits sorted in ascending order:", fruits) 

#Sorting the list in descending order
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits.sort(reverse=True)
print("Q5.4 - Fruits sorted in descending order:", fruits)

# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.Sample List : ['abc', 'xyz', 'aba', '1221']
def count_special_strings(string_list):
    count = 0
    for string in string_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Sample list
string_list = ['abc', 'xyz', 'aba', '1221']

result = count_special_strings(string_list)
print("Number of special strings:", result)

#TUPLES IN PYTHON:
#Practice wuestions
#question 1
 fruits = ["apple", "banana", "cherry"]
 first_fruit = fruits[0] 
 last_fruit = fruits[-1] 

#question 2
 numbers = [1, 2, 3, 4, 5]
 sublist1 = numbers[1:4]  
 sublist2 = numbers[2:] 
 sublist3 = numbers[-3:] 

#Write a Python program to replace the last value of tuples in a list.Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
 def replace_last_value(tuple_list, new_value):
    return [tuple(list(t)[:2] + [new_value]) for t in tuple_list]

# Sample list
 tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

 new_value = 100
 result = replace_last_value(tuple_list, new_value)
 print("Updated list:", result)

# Write a Python program to convert a tuple of string values to a tuple of integer values. Original tuple values: (('333', '33'), ('1416', '55')) New tuple values: ((333, 33), (1416, 55))
 def convert_tuple_values(tuple_of_tuples):
    return tuple(tuple(int(value) for value in inner_tuple) for inner_tuple in tuple_of_tuples)

# Original tuple values
 original_tuple = (('333', '33'), ('1416', '55'))

new_tuple = convert_tuple_values(original_tuple)
print("New tuple values:", new_tuple)

#explaining tuples:
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Indexing and slicing
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slice from index 1 to 3:", my_tuple[1:3])

# Tuple methods
print("Length of the tuple:", len(my_tuple))
print("Maximum value in the tuple:", max(my_tuple))
print("Minimum value in the tuple:", min(my_tuple))

# Tuple functions
print("Tuple with repeated elements:", (1, 2) * 3)
print("Concatenated tuples:", (1, 2) + (3, 4))

# Tuple membership testing
print("Is 3 in the tuple?", 3 in my_tuple)
print("Is 6 in the tuple?", 6 in my_tuple)

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# Tuple modification (note: tuples are immutable)
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

# Converting a list to a tuple
my_list = [1, 2, 3]
my_tuple_from_list = tuple(my_list)
print("Tuple from list:", my_tuple_from_list)

# Converting a tuple to a list
my_list_from_tuple = list(my_tuple)
print("List from tuple:", my_list_from_tuple)

#NARIES IN PYTHON:
# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print("Original dictionary:", my_dict)

# Accessing dictionary elements
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Updating dictionary elements
my_dict["age"] = 31
print("Updated dictionary:", my_dict)

# Adding new dictionary elements
my_dict["country"] = "USA"
print("Updated dictionary:", my_dict)

# Removing dictionary elements
del my_dict["city"]
print("Updated dictionary:", my_dict)

# Dictionary methods
print("Dictionary keys:", my_dict.keys())
print("Dictionary values:", my_dict.values())
print("Dictionary items:", my_dict.items())

# Checking if a key exists in the dictionary
print("Is 'name' a key in the dictionary?", "name" in my_dict)
print("Is ' occupation' a key in the dictionary?", "occupation" in my_dict)

# Getting a dictionary element with a default value
print("Occupation:", my_dict.get("occupation", "Not specified"))

# Dictionary functions
print("Dictionary with updated values:", dict(name="Jane", age=25, city="London"))

# Merging two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print("Dictionary comprehension:", squares)

# Dictionary unpacking
dict3 = {"e": 5, "f": 6}
{**dict1, **dict3}
print("Unpacked dictionary:", dict1)

# Converting a dictionary to a list of tuples
list_of_tuples = list(my_dict.items())
print("List of tuples:", list_of_tuples)

# Converting a list of tuples to a dictionary
dict_from_list = dict(list_of_tuples)
print("Dictionary from list:", dict_from_list)

#practice questions
#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Sample data : {'1':['a','b'], '2':['c','d']} Expected Output: ac ad bc bd
import itertools

def combine_letters(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    combinations = itertools.product(*values)
    for combination in combinations:
        print(''.join(combination))

# Sample data
data = {'1':['a','b'], '2':['c','d']}
combine_letters(data)

#Write a Python program to create a dictionary from a string. sample string : 'w3resource' Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
def string_to_dict(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Sample string
s = 'w3resource'
print(string_to_dict(s))

#Write a Python program to convert a list into a nested dictionary of keys.
def list_to_nested_dict(lst):
    result = {}
    for item in lst:
        current = result
        for key in item[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[item[-1]] = {}
    return result

# Sample list
lst = [['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'e', 'f'], ['g', 'h', 'i']]
print(list_to_nested_dict(lst))

#Write a Python program to print a dictionary in table format.
def print_dict_table(d):
    print("{:<10} {:<10}".format("Key", "Value"))
    print("-" * 20)
    for key, value in d.items():
        print("{:<10} {:<10}".format(key, value))

# Sample dictionary
d = {"Name": "John", "Age": 30, "City": "New York", "Country": "USA"}
print_dict_table(d)


#SETS IN PYTHON:
#Creating a Set in Python
# Creating a Set with the use of a String
set1 = set("GeeksForGeeks")
print("Set with the use of String: ")
print(set1)

# Creating a Set with the use of an Object
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: ")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

# Creating a Set with the use of a tuple
t = ("Geeks", "for", "Geeks")
print("\nSet with the use of Tuple: ")
print(set(t))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print("\nSet with the use of Dictionary: ")
print(set(d))

#set operations in python
# Define two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

### Union ###
print("Union:", A.union(B)) 
print("Union (using | operator):", A | B) 

### Intersection ###
print("Intersection:", A.intersection(B))  
print("Intersection (using & operator):", A & B)  

### Difference ###
print("Difference (A - B):", A.difference(B)) 
print("Difference (A - B) using - operator:", A - B)
### Symmetric Difference ###
print("Symmetric Difference:", A.symmetric_difference(B)) 
print("Symmetric Difference using ^ operator:", A ^ B)  

#set method in python
# Define a set
my_set = {1, 2, 3, 4, 5}

### 1. Add method ###
my_set.add(6)
print("After adding 6:", my_set)  

### 2. Update method ###
my_set.update([7, 8, 9])
print("After updating with [7, 8, 9]:", my_set)  

### 3. Remove method ###
my_set.remove(4)
print("After removing 4:", my_set)  

### 4. Discard method ###
my_set.discard(5)
print("After discarding 5:", my_set) 

### 5. Pop method ###
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After popping:", my_set)

### 6. Clear method ###
my_set.clear()
print("After clearing:", my_set)  

### 7. Union method ###
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union of set1 and set2:", set1.union(set2))  

### 8. Intersection method ###
print("Intersection of set1 and set2:", set1.intersection(set2))  

### 9. Difference method ###
print("Difference of set1 and set2:", set1.difference(set2)) 

### 10. Symmetric Difference method ###
print("Symmetric difference of set1 and set2:", set1.symmetric_difference(set2))

### 11. Subset method ###
set3 = {1, 2}
print("Is set3 a subset of set1?", set3.issubset(set1))  

### 12. Superset method ###
print("Is set1 a superset of set3?", set1.issuperset(set3))  

#set comprehension in python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = {num for num in numbers if num % 2 == 0}
print(even_numbers)  

#set operations in python 
#cartesian product
def cartesian_product(set1, set2):
    return {(a, b) for a in set1 for b in set2}

set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
print(cartesian_product(set1, set2))

#power set 
def power_set(frozenset_input):
    power_set = [[]]
    for element in frozenset_input:
        new_subsets = []
        for subset in power_set:
            new_subset = subset + [element]
            new_subsets.append(new_subset)
        power_set.extend(new_subsets)
    return [frozenset(subset) for subset in power_set]

frozen_set = frozenset([1, 2, 3, 4])
print(power_set(frozen_set))  

#Set Algebra (SymPy's BooleanAlgebra)
from sympy.logic.boolalg import BooleanAlgebra

ba = BooleanAlgebra()

# Define sets
A = ba.Symbol('A')
B = ba.Symbol('B')
C = ba.Symbol('C')

# Union
print(ba.Or(A, B))  

# Intersection
print(ba.And(A, B))  

# Difference
print(ba.And(A, ba.Not(B))) 

# Symmetric Difference
print(ba.Xor(A, B)) 