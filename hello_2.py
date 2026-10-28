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

# Using external packages

# web requests
import requests

response = requests.get("https://api.example.com/data")
data = response.json()

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# Common mistakes to avoid
# Wrong - overwrites built-in
import datetime
datetime = "2024-01-01"  # Now module is gone!

# Right - use different names
import datetime
date_string = "2024-01-01"

# Working with APIs
# pull data from web services

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)
data["current"]

# building something from the above
import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")


# Try and except
# This will throw an error
result = 10/0 # Zero Divison

# use try and except to manage errors gracefully
try:
    result = 10/0 # Zero Divison
except:
    print("Hi there!")


# Catching specific errors
# This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here

# Multiplle error types:
try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Using the else clause:
# Code in else runs only if no error happened:
try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")


# The finally clause
# Code in finally always runs, error or not:
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs to clean up
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete")

# N.B: Don’t catch all errors with a bare except:. It hides problems and makes debugging harder. Always catch specific error types when possible.

def process_data():
    print("process_data ...")
    pass


def risky_operation():
    print("risky_operation ...")
    pass


def critical_operation():
    print("critical_operation ...") 

# Common Mistake:

# catching too broad exceptions:
# Bad - catches everything
try:
    process_data()
except:
    pass  # Silent failure!

# Good - specific error
try:
    process_data()
except ValueError:
    print("Invalid data format")

# Empty except blocks
# Bad - ignores the error
try:
    risky_operation()
except ValueError:
    pass

# Good - at least log it
try:
    risky_operation()
except ValueError:
    print("Warning: Invalid value encountered")


# Not re-raising critical errors
# Bad - hides all errors
try:
    critical_operation()
except Exception as e:
    print(f"Error: {e}")

# Good - log and re-raise
try:
    critical_operation()
except Exception as e:
    print(f"Critical error: {e}")
    raise  # Let the error propagate


# Common errors:
# FileNotFoundError: happens when a file doesn't exist
# This fails if file doesn't exist
with open('missing.txt', 'r') as f:
    content = f.read()

# Fix:
import os

# Check first
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        content = f.read()
else:
    print("File not found")

# Or use try-except
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = ""  # Default value


# ValueError: Happens when a value is wrong type or format:

# These cause ValueError
int("hello")        # Can't convert to number
int("12.5")         # int() doesn't accept decimals
list.remove("x")    # Item not in list

# Fix:
# Validate user input
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number")

# Convert carefully
float_str = "12.5"
number = int(float(float_str))  # Convert to float first

# KeyError: Happens when a dictionary key doesn’t exist:
user = {"name": "Alice", "age": 25}
print(user["email"])  # KeyError - no email key

# Fix:
# Check if key exists
if "email" in user:
    print(user["email"])

# Use get() with default
email = user.get("email", "no-email@example.com")

# Or handle the error
try:
    print(user["email"])
except KeyError:
    print("Email not found")

# IndexError: Happens when accessing invalid list position:
numbers = [1, 2, 3]
print(numbers[5])  # IndexError - only 3 items

# Fix:
# Check length first
if len(numbers) > 5:
    print(numbers[5])

# Use negative indexing carefully
last_item = numbers[-1] if numbers else None

# Handle the error
try:
    print(numbers[5])
except IndexError:
    print("List too short")


# TypeError: Happens when operations use wrong types:
# These cause TypeError
value = "hello" + 5            # Can't add string and number
len(42)                # Numbers don't have length
int([1, 2, 3])         # Can't convert list to int

# Fix:
# Convert types explicitly
"hello" + str(5)       # "hello5"
str(42)                # "42"

# Check type first
if isinstance(value, str):
    print(len(value))

# AttributeError: Happens when accessing non-existent attributes:
text = "hello"
text.append("!")  # AttributeError - strings don't have append

# Use correct methods
text = "hello"
text = text + "!"  # Strings are immutable

# Check if attribute exists
if hasattr(text, 'append'):
    text.append("!")


# Inheritance :: class
# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())   # Buddy says woof!


# Adding attributes in child classes
# Child classes can have their own attributes too:

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Pass name to parent's __init__
        self.breed = breed      # Dog-specific attribute

    def describe(self):
        return f"{self.name} is a {self.breed}"

    # Create dogs with breed - positional arguments
golden = Dog("Buddy", "Golden Retriever")

    # Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe())    # Buddy is a Golden Retriever
print(golden.is_pet)        # True (inherited from Animal)

# Overriding methods
# Child classes can change how parent methods work:

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self)     :
        return f"{self.name} makes a sound"

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow!"

# Different animals, different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.make_sound())  # Something makes a sound
print(dog.make_sound())      # Buddy barks: Woof!
print(cat.make_sound())      # Whiskers meows: Meow!

# Real-world use case
# Here's a practical example for AI applications:
class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False
    
    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True

class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length
    
    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # Truncate if needed
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed: {text}"

# Use the model - with named arguments
model = TextModel(model_name="gpt-3.5-turbo", max_length=100)

# Call method - notice no 'self' parameter needed
result = model.process_text(text="Hello world")
print(result)  # Loading gpt-3.5-turbo...
               # Processed: Hello world

# Common mistakes
# Forgetting to call super().init()
# Wrong - parent's __init__ not called
class Parent:
    pass

class Child(Parent):
    def __init__(self, name):
        self.name = name  # Parent attributes missing!

# Right - call parent's __init__
class Child(Parent):
    def __init__(self, name):
        super().__init__()
        self.name = name


# Wrong inheritance relationship
# Wrong - Rectangle is not a Square!
class Square:
    def __init__(self, size):
        self.size = size

class Rectangle(Square):  # Doesn't make sense
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Better - they're both shapes
class Shape:
    pass

class Square(Shape):
    def __init__(self, size):
        self.size = size

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


# When to use classes
# Functional programming
# Functions operate on data
def clean_text(text):
    return text.strip().lower()

def remove_punctuation(text):
    return text.replace(".", "").replace(",", "")

# Chain functions together
result = remove_punctuation(clean_text("  Hello, World.  "))

# Object-oriented programming -Using classes to bundle data and behavior
# Class bundles data and methods
class TextProcessor:
    def __init__(self, text):
        self.text = text
    
    def clean(self):
        self.text = self.text.strip().lower()
        return self
    
    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self

# Chain methods on object
processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text