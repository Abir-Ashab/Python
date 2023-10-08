# it is more like map or structure

identity = {'name' : 'niloy', 'age' : 22, 'city' : 'dhaka'}
# syntax : key : value

print(identity.keys())
for i in identity.keys(): 
    print(i)

print(identity.values())
for i in identity.values(): 
    print(i)

# both keys and values
print(identity.items())
for i in identity.items(): 
    print(i)
for i, j in identity.items(): 
    print(i, j)

# coverting to list
x = list(identity.keys())
y = list(identity.values())
print(x, y)

# use of in keyword
is_name = 'name' in identity
print(is_name)

# get method
print(str(identity.get('name', 'DEFAULT')))
print(str(identity.get('city', 'DEFAULT')))
# if not present, it will not print
print(str(identity.get('country', 'DEFAULT')))

# if name, city, country is present print the presented one, else set kalam, ctg, BD
print(str(identity.setdefault('name', 'kalam')))
print(str(identity.setdefault('city', 'ctg')))
# if not present, it will not print
print(str(identity.setdefault('country', 'BD')))

print(identity)








# gpt codes 

# Create an empty dictionary
my_dict = {}

# Create a dictionary with key-value pairs
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing dictionary values by key
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Modifying dictionary values
person["age"] = 31
person["city"] = "San Francisco"

# Adding new key-value pairs
person["country"] = "USA"

# Deleting key-value pairs
del person["country"]

# Checking if a key exists
if "country" in person:
    print("Country:", person["country"])
else:
    print("Country key not found.")

# Iterating over keys
for key in person:
    print(key, "=", person[key])

# Iterating over key-value pairs
for key, value in person.items():
    print(key, "=", value)

# Getting a list of keys
keys = person.keys()
print("Keys:", keys)

# Getting a list of values
values = person.values()
print("Values:", values)

# Getting the number of key-value pairs
num_items = len(person)
print("Number of items:", num_items)

# Clearing a dictionary
person.clear()

# Nested dictionaries
student = {
    "name": "Alice",
    "courses": {
        "math": 90,
        "science": 85,
        "history": 88
    }
}

# Accessing values in a nested dictionary
math_score = student["courses"]["math"]
print("Math score:", math_score)