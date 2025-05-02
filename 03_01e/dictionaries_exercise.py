# Basic Dictionary Operations

# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict["name"] = "Alice"
my_dict["age"] = 25
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Access a value using a key
print(my_dict["name"])  # Output: Alice

# Modify an existing value
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Check if a key exists
if "city" in my_dict:
    print("City:", my_dict["city"])  # Output: City: New York

if "country" not in my_dict:
    print("Key 'country' not found")  # Output: Key 'country' not found

# Remove a key-value pair using del
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}

# Remove a key-value pair using pop (also returns the value)
age = my_dict.pop("age")
print(age)  # Output: 26
print(my_dict)  # Output: {'name': 'Alice'}

# Add more items
my_dict["profession"] = "Engineer"
my_dict["hobby"] = "Painting"

# Iterate through dictionary keys
for key in my_dict:
    print(key, "->", my_dict[key])
# Output:
# name -> Alice
# profession -> Engineer
# hobby -> Painting

# Iterate through dictionary values
for value in my_dict.values():
    print(value)
# Output:
# Alice
# Engineer
# Painting

# Iterate through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# profession: Engineer
# hobby: Painting
