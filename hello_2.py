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
