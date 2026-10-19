# First, create a variable
message = "Hello"

# Later, use it (even in a different cell)
print(message + " World!")

# Modify it
message = message.upper()
print(message)

# more string manipulations
print(len(message))

empty = ""
print(len(empty))


# Converting other types to string
age = 25
message = "I am "+ str(age) + " years old"
print(message) 

# Or use f-strings
message = f"I am {age} years old"
print(message)


# This is a comment in python
# called a single line comment: This is another comment

"""

This is a multiline comment in python which is a multiline quote that can go on and on.

"""
print("hello world")

first_name = "Alice"

user_age = 25

first_name = "Dave"

print("Your name is ", {first_name})


total = 10 - 7
print(total)

# Implement arithmetic calculations: use interactive jupyter
10 - 7
6 * 6
10**2 

# String
my_string = "My name is Henry"

my_long_string = """
My name is Henry.
My last name is Erabor
"""

print(my_long_string)

first_name = "Henry"
last_name = "Erabor"

full_name = first_name + " " + last_name
full_name
print(full_name)

long_dash = "-" * 30
print(full_name)
print(long_dash)
len(first_name)
 
# Playing around with Boolean values
is_logged_in = False
is_true = True

age = 18

can_vote = age >= 18

is_18 = age == 18


# Quick demonstration of multiline comments with a simple function

"""
This is a multi-line comment.
It can span several lines.
Great for longer explanations.
"""
def calculate_tip(bill):
    """
    Calculate 20% tip for a restaurant bill.
    Takes the bill amount and returns the tip.
    """
    return bill * 0.20


# Good comments explain WHY, not WHAT:
subtotal = 1000
# Good: Explains why
# Using 1.0625 because sales tax in CA is 6.25%
total = subtotal * 1.0625

# Bad: States the obvious
# Multiply subtotal by 1.0625
total = subtotal * 1.0625


# Check different types
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# Check variables
age = 25
name = "Alice"
print(type(age))         # <class 'int'>
print(type(name))        # <class 'str'>


# Logical operators

age = 25
has_license = True
drunk = True


# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

can_drive = age >= 16 and has_license and not drunk
print(can_drive)

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend) # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child) # False

# Assignment shortcuts
score, total = 7, 14

# Instead of:
score = score + 10

total = total * 2

# Write:
score += 10
print(score)
total *= 2
print(total)

# Workng with text/string

# Concatenation:
first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"

# Repetition
stars = "*"
stars = stars * 10 

separator = "-" * 20

print(stars) 
print(separator)


# Some String methods
# Changing case
text = "Python Programming"

print(text.lower())      # "python programming"
print(text.upper())      # "PYTHON PROGRAMMING"
print(text.title())      # "Python Programming"


# Cleaning strings
messy = "  hello world  "
print(messy.strip())     # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"

# Finding and replacing
message = "I love Python programming with Python"

# Check if something exists
print("Python" in message) # True
print(message.startswith("I")) # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))  # 7 (first occurrence index wise)
print(message.count("Python")) # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message) # "I love JavaScript programming with JavaScript"

# Control flow
temperature = 31

if temperature > 30:
    print("It's very hot!")
elif temperature > 25:
    print("It's hot!")
else:
    print("It's nice weather!")


score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")


# multiple condition
age = 25
has_license = True
weekend = True
holiday = True
raining = False

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")

# nested if statements
has_tickets = True
age = 15

if has_tickets:
    if age >= 18:
        print("Enjoy the movie")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")


# For Loops
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)


# loop through text
name = "Python"
for letter in name:
    print(letter)
    print(type(letter))

# loop throgh a list
colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")

# while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1


# Data Structure
# Lists
# Dictionaries
# Tuples
# Sets


# Lists: all types of data with different types of types
age = 25
has_license = False
my_list = ["Alice", 25, age, True, has_license]

name = my_list[0]
age = my_list[1]

has_license = my_list[3]

# Accessing items
fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])   # ["banana", "orange"]


# Changing list: lists are mutable

fruits = ["apple", "banana", "orange"]

# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")      # Add to end
fruits.insert(1, "kiwi")    # Insert at position

# Remove items
fruits.remove("banana")     # Remove by value
last = fruits.pop()        # Remove and return last
del fruits[0]              # Remove by index


# List methods
numbers = [3, 2, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              #[1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 2, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy
print(new_list)

# Short intro to using List comprehension
# It's dangerous to change list size while looping through

#  Wroong way of filtering out an item in a list
numbers = [1, 2, 3, 4]
for num in numbers:
    if num == 2:
        numbers.remove(num) # Dangerous

print(numbers)

# Right way : using List comprehension
numbers = [1, 2, 3, 4]
numbers = [num for num in numbers if num!= 2] # List comprehension

print(numbers)

# Shallow copy issues:
# Wrong both variables point to the same list
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1) # [1, 2, 3, 4] - list1 - changed

# Right - make a copy
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1) # [1, 2, 3] - unchanged


# Dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

person["name"] = "Dave"
person["license"] = True

print(person)

del person["license"]

