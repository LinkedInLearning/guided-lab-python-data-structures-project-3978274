# Basic List Operations

# Create an empty list
my_list = []

# Append elements to the list (adding items to the end)
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)  # Output: [10, 20, 30]

# Access an element by index
print(my_list[1])  # Output: 20

# Modify an element
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30]

# Insert an element at a specific index
my_list.insert(1, 15)
print(my_list)  # Output: [10, 15, 25, 30]

# Remove an element by value
my_list.remove(25)
print(my_list)  # Output: [10, 15, 30]

# Remove and return an element by index using pop.
# No argument means pop last element.
last_element = my_list.pop()
print(last_element)  # Output: 30
print(my_list)  # Output: [10, 15]

# Check if an element exists
if 10 in my_list:
    print("10 is in the list")  # Output: 10 is in the list

# Iterate through the list
for item in my_list:
    print(item)  # Output: 10  15

# Find the length of the list
print(len(my_list))  # Output: 2

# Reverse a list
my_list.reverse()
print(my_list)  # Output: [15, 10]

# Sort a list
numbers = [5, 3, 8, 1, 4]
numbers.sort()
print(numbers)  # Output: [1, 3, 4, 5, 8]

# Create a new sorted list without modifying the original
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [8, 5, 4, 3, 1]
print(numbers)  # Output: [1, 3, 4, 5, 8] (unchanged)

# Create a list comprehension (squares of numbers from 1 to 5)
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
