# Basic Tuple Operations

# Create an empty tuple
my_tuple = ()

# Create a tuple with multiple elements
my_tuple = (10, 20, 30)
print(my_tuple)  # Output: (10, 20, 30)

# Access an element by index
print(my_tuple[1])  # Output: 20

# Count occurrences of an element
count_20 = my_tuple.count(20)
print(count_20)  # Output: 1

# Find the index of an element
index_30 = my_tuple.index(30)
print(index_30)  # Output: 2

# Check if an element exists
if 10 in my_tuple:
    print("10 is in the tuple")  # Output: 10 is in the tuple

# Iterate through the tuple
for item in my_tuple:
    print(item)  # Output: 10  20  30

# Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5)

# Slice a tuple (extract elements from index 1 to 2)
sliced_tuple = my_tuple[1:3]
print(sliced_tuple)  # Output: (20, 30)

# Create a tuple with different data types
mixed_tuple = (10, "hello", [1, 2, 3])
print(mixed_tuple)  # Output: (10, 'hello', [1, 2, 3])

# Length of a tuple
print(len(my_tuple))  # Output: 3

# Attempting to modify a tuple raises an error
# my_tuple[1] = 25  # Uncomment to see: TypeError: 'tuple' object does not support item assignment

# Unpack tuple elements into variables
a, b, c = my_tuple
print(a, b, c)  # Output: 10 20 30

# Create a tuple comprehension (using generator with tuple())
squares = tuple(x ** 2 for x in range(1, 6))
print(squares)  # Output: (1, 4, 9, 16, 25)