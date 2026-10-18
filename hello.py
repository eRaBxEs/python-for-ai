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

