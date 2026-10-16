# First, create a variable
message = "Hello"

# Later, use it (even in a different cell)
print(message + " World!")

# Modify it
message = message.upper()
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