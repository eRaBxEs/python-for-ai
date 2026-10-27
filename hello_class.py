
# class Dog
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# class Cat
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


# create an object which is an instance of the class Dog
# using positional arguments
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# or with named arguments clearer
jerry = Dog(name="Jerry", breed="Labrador")

jerry.breed
print(dog1.name)
print(dog2.breed)

# Real-World example: configuration
class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000

# APIConfig is the class
# config1 and config2 are instances
config1 = APIConfig(api_key="key1", max_tokens=50)
config2 = APIConfig(api_key="key2", max_tokens=200)

# Each instance has its own data
print(config1.max_tokens)  # 50
print(config2.max_tokens)  # 200

# Changing one doesn't affect the other
config1.max_tokens = 75
print(config1.max_tokens)  # 75
print(config2.max_tokens)  # 200 (unchanged)

# Methods and attributes
# Notes: A class is a blueprint for creating objects. It defines:
    # Attributes: What data the object stores
    # Methods: What the object can do
# Attributes are variables that belong to an object

class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key      # Each client has its own key
        self.base_url = base_url    # Each client has its own URL
        self.request_count = 0      # Track requests per client

# Creating instances with named arguments
client1 = APIClient(api_key="key1", base_url="https://api1.com")
client2 = APIClient(api_key="key2", base_url="https://api2.com")


# Class attributes (shared by all objects) 
class APIClient:
    version = "1.0"     # Same for all clients
    max_retires = 3     # Same for all clients


    def __init__(self, api_key):
        self.api_key = api_key  # Unique to each client


"""
Methods are functions that belong to a class. 
They always have self as the first parameter, but you don’t pass it when calling:
"""

class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']


class Goat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Bleat!!!")

goatie = Goat(name="goatie")
goatie.name

goatie.sound()