# Defining a function
def greet():
    print("Hello!!")
    print("Hello again!")
    pass

greet()


"""
Naming functions
Follow these rules for function names:
    i.   Use lowercase letters
    ii.  Separate words with underscores
    iii. Be descriptive about what it does
"""

# Good names
def calculate_total():
    pass

def send_email():
    pass

def validate_password():
    pass

# Bad names
def func1():  # Not descriptive
    pass

def Calculate():  # Should be lowercase
    pass

# Calling functions
def say_goodbye():
    print("Goodbye!")
    print("See you later!")

# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()

def check_weather():
    temperature = 16
    if temperature > 25:
        print("It's hot!")
    else:
        print("It's nice weather!")
    pass

# Use the function
check_weather()

# Variable Scope: Local vs Global
# Local variable
def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
# print(price)  # NameError: name 'price' is not defined

# Global variable
discount_rate = 0.15  # Global variable

def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount

result = apply_discount(100)
print(result)  # 85.0

# Modifying global variable
# To change a global variable inside a function, use the global keyword:
counter = 0 # Global variable
def increment():
    global counter # declare that we want to modify the global variable
    counter += 1
    pass

increment()
increment()
print(counter) # 2


# Bad -using global variable
total = 0

def add_to_total(amount):
    global total
    total += amount
    pass

# Good -using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total) # 30


# Parameters: passing data into your functions
# Without parameters (inflexible)
def greet_alice():
    print("Hello, Alice!")

# With parameters (flexible)
def greet(name):
    print(f"Hello, {name}!")

# Now it works for anyone
greet("Alice")
greet("Bob")
greet("Charlie")


def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")
    pass

greet_user("Dave", "Benard") # defalt use
greet_user(last_name="Erabor", first_name="Henry") # swapping the argument/parameter

# using a default value
def greet_again(last_name, first_name="John"):
    print(f"Hello, {first_name} {last_name}")
    pass
greet_again(last_name="Erabor")

def greet_him(last_name = "Doe", first_name="John"):
    print(f"Hello, {first_name} {last_name}")
    pass

greet_him()

# overwrite the default argument
greet_him(first_name="Jesus")

# multiple parameters
def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")

# Call with values
introduce("Alice", 25)
introduce("Bob", 30)

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10)  # $98

# Keyword vs Positional arguments
def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)

# Common mistakes
def greet(name, age):
    print(f"Hi {name}, you're {age}")

# Wrong - too few arguments
greet("Alice")  # TypeError!

# Wrong - too many arguments
greet("Alice", 25, "NYC")  # TypeError!

# Right
greet("Alice", 25)

# Wrong - don't use lists as defaults
def add_item(item, list=[]):
    list.append(item)
    return list

# Right - use None and create new list
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list


counter = 0 # Global variable
def increment():
    counter # we failed to declare that we want modify (mutate) the global variable
    counter += 1 # so this throws an error
    pass

increment()
increment()
print(counter) # 2



discount = 10
def calculate_total_again(price):
    # You necessarily dont need to declare using global keyword to indicate that you want to use the global variable
    # global discount is not needed because we are not modifying the value of the global discount, so no error.
    tax_rate = 0.08

    #Calculation
    tax = price * tax_rate
    final_price = price + tax - discount

    # Print the final price
    print(f"Total: ${final_price}")
    pass

calculate_total_again(price=100)

# return statement

def add_print(a, b):
    print(a + b)

add_print(a=5, b=10)

def add_return(a, b):
    return a + b

result = add_return(a=5, b=10)
print(f"The result is {result}") # The result is 15

# use return to send value back from a function

def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft

# Return multiple values
def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

f, l = simple_function()
print(f)
print(l)

# more on returning multiple values
def get_min_max(numbers):
    #print(type(numbers))
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)

# Functions without explicit return statements return None:
def greet(name):
    print(f"Hello, {name}!")
    # No return statement

result = greet("Alice")  # Prints: Hello, Alice!
print(result)  # None

# Common mistake
# Wrong - prints instead of returning
def multiply(a, b):
    print(a * b)

result = multiply(3, 4)  # Prints 12
total = result + 10      # Error! result is None

# Right - return the value
def multiply(a, b):
    return a * b

# Import packages
# Pattern 1: Import the whole module
import math
# Now use: 
math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: 
sqrt(16)

import random

number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])

# Common built-in modules
# Date and time
import datetime
today = datetime.date.today()
print(today) # 2026-10-22

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

# Import methods
# Import entire module
import math
result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi
result = sqrt(16)
radius = 25
circle_area = pi * radius ** 2

# Import with alias
import pandas as pd
df = pd.DataFrame(data)

# Import everything (avoid this!)
from math import *

# Always ensure your virtual environment is activated before installing!
# Install a package
#pip install requests

# Install specific version
#pip install requests==2.28.0

# Install multiple packages
#pip install pandas numpy matplotlib

# Sharing yyour project requiremnts
#pip freeze > requirements.txt : list all your project's packages
#pip install -r requirements.txt : to get printed all your project requirements on a text file